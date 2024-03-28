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
// /////////////////////////////////

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


// $(document).ready(function () {
//     $('#delete-pic').click(function () {
//         // Perform delete action
//         $.ajax({
//             url: '/profile/delete_profile_pic', // Update with your delete endpoint
//             type: 'POST',
//             success: function (response) {
//                 // Reload the page
//                 window.location.reload();
//             },
//             error: function (xhr, status, error) {
//                 // Handle error, such as displaying an error message
//                 console.error('Error deleting profile picture.');
//             }
//         });
//     });
// });

// $(document).ready(function () {
//     $(document).on('click', '#delete-pic', function () {
//         console.log('Delete button clicked'); // Check if this message appears in the console
//         // Perform delete action
//         $.ajax({
//             url: '/profile/delete_profile_pic', // Update with your delete endpoint
//             type: 'POST',
//             success: function (response) {
//                 console.log('Profile picture deleted successfully'); // Log success message
//                 // Reload the page
//                 window.location.reload();
//             },
//             error: function (xhr, status, error) {
//                 // Handle error, such as displaying an error message
//                 console.error('Error deleting profile picture:', error);
//             }
//         });
//     });
// });



function deleteProfilePic() {
    // console.log('Delete button clicked');

    $.ajax({
        url: '/profile/delete_profile_pic',
        type: 'POST',
        success: function (response) {
            // console.log('Profile picture deleted successfully');
            window.location.reload();
        },
        error: function (xhr, status, error) {
            // console.error('Error deleting profile picture:', error);
        }
    });
}
