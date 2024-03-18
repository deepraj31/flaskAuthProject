import os
import secrets
from flask import current_app, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user
from app import app
from models import User, db
from flask_login import login_required
from PIL import Image


@app.route('/')
def index():
    user_id = db.session.execute(db.select(User).order_by(User.id)).scalars()
    return render_template('index.html', user=current_user)





@app.route('/profile')
@login_required
def profile():
    profile_pic = current_user.profile_pic
    return render_template('profile.html', profile_pic=profile_pic)

@app.route('/profile/profile_pic/upload', methods=['POST'])
@login_required
def profilePicUpload():
    picture_file = request.files['image']

    if picture_file:
        # Check if the user already has a profile picture
        if current_user.profile_pic != 'default.jpg':
            # Remove the old profile picture from the directory
            old_picture_path = os.path.join(current_app.root_path, 'static/profile_pic', current_user.profile_pic)
            if os.path.exists(old_picture_path):
                os.remove(old_picture_path)

        # Generate a random filename
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(picture_file.filename)
        picture_filename = random_hex + f_ext
        picture_path = os.path.join(current_app.root_path, 'static/profile_pic', picture_filename)

        # Compress the image
        compressed_image = compress_image(picture_file)

        # Save the compressed image
        compressed_image.save(picture_path)

        # Update the user's profile picture in the database
        current_user.profile_pic = picture_filename
        db.session.commit()

        flash('Your profile picture has been updated!', 'success')
    else:
        # No file selected, show a flash message
        flash('You did not select any image!', 'warning')

    return redirect(url_for('profile'))

def compress_image(image_file):
    # Open the image file
    img = Image.open(image_file)

    # Set the maximum size for the compressed image
    max_size = (600, 600)  # Adjust the size as needed

    # Resize the image
    img.thumbnail(max_size)

    # Return the compressed image
    return img




@app.route('/profile/delete_profile_pic', methods=['POST'])
@login_required
def deleteProfilePic():
    if current_user.profile_pic != 'default.jpg':
        # Delete the current user's profile picture
        picture_path = os.path.join(current_app.root_path, 'static/profile_pic', current_user.profile_pic)
        if os.path.exists(picture_path):
            os.remove(picture_path)
            current_user.profile_pic = 'default.jpg'
            db.session.commit()
            flash('Your profile picture has been deleted!', 'success')
        else:
            flash('Error deleting profile picture.', 'danger')
    else:
        flash('You cannot delete the default profile picture!', 'warning')

    return jsonify(message='Profile picture deleted successfully!')

