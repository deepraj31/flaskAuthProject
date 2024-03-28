// Automatically remove flashed messages after 3 seconds
setTimeout(function () {
    document.querySelectorAll('.alert').forEach(function (alert) {
        alert.remove();
    });
}, 3000);



// Password Field toggle type txt to pass
const passwordField = document.getElementById('passwordField');
const togglePassword = document.getElementById('togglePassword');

const confirmPasswordField = document.getElementById('confirmPasswordField');
const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');

togglePassword.addEventListener('click', function () {
    togglePasswordVisibility(passwordField, this);
});

toggleConfirmPassword.addEventListener('click', function () {
    togglePasswordVisibility(confirmPasswordField, this);
});


function togglePasswordVisibility(field, icon) {
    const type = field.getAttribute('type') === 'password' ? 'text' : 'password';
    field.setAttribute('type', type);
    icon.classList.toggle('bi-eye');
    icon.classList.toggle('bi-eye-slash');
}


function toggleUploadForm() {
    var uploadForm = document.getElementById("upload-image-form");
    var overlay = document.getElementById("overlay");
    if (uploadForm.style.display === "none") {
        uploadForm.style.display = "block";
        overlay.style.display = 'block'
    } else {
        uploadForm.style.display = "none";
        overlay.style.display = 'none'
    }

}




function deleteProfilePic() {
    $.ajax({
        url: '/profile/delete_profile_pic',
        type: 'POST',
        success: function (response) {
            window.location.reload();
        },
        error: function (xhr, status, error) {
        }
    });
}
