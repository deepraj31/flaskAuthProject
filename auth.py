
from flask import flash, redirect, render_template, request, url_for, session


from app import app

from models import User, db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user

bcrypt = Bcrypt(app)

# LoginManager is needed for our application to be able to log in and out users
login_manager = LoginManager()
login_manager.init_app(app)


# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    flash('Please log in to access this page.', 'warning')
    return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        cpassword = request.form['cpassword']
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already Registered', 'danger')
            return redirect(url_for('login'))
        elif len(password) < 6:
            flash('Password is to short!', 'danger')
        elif password != cpassword:
            flash("Password didn't Matched!", 'danger')
        else:
            hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
            newUser = User(fname=fname, lname=lname, email=email, phone=phone, password=hash_password)
            db.session.add(newUser)
            db.session.commit()
            flash("Registration Successfull!", 'success')
            return redirect(url_for('login'))




    return render_template('auth/register.html')





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        # Check if the password entered is the same as the user's password
        if user:
            is_valid = bcrypt.check_password_hash(user.password, password)
            if is_valid:
                # Use the login_user method to log in the user
                login_user(user)
                flash("Logged In Successfull!", 'success')
                return redirect(url_for("index"             ))
                # Redirect the user back to the home
                # (we'll create the home route in a moment)
            else:
                flash("Invalid Email Or Password!", 'danger')
        else:
            flash("User Not Found!", 'danger')
    return render_template('auth/login.html')





@app.route('/logout')
def logout():
    logout_user()
    flash("Logged Out Successfully!", 'info')
    return redirect(url_for('login')) 





# ///////////////////////
