# User Authentication System 
**Simple project for authenticate user and dynamically show the fields and links according to the current user**

This project is a simple user authentication system built using Flask, SQLAlchemy, Flask-Login, and Flask-Bcrypt. It allows users to register, login, update their profile information, upload and delete their profile picture, and delete their account.

## Features

- **User Registration:** Users can register by providing their first name, last name, email, phone number, and password.
- **User Login:** Registered users can log in using their email and password.
- **Profile Update:** Users can update their profile information including their first name, last name, email, phone number, and address.
- **Profile Picture:** Users can upload a profile picture, update it, or delete it.
- **Account Deletion:** Users can delete their account, which also deletes their profile information and profile picture.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- HTML/CSS/JavaScript/JQuery/AJAX (for front-end)

## Usage

- Register a new account by providing the required information.
- Log in using your registered email and password.
- Update your profile information or upload/delete your profile picture.
- Delete your account if needed.



## Folder Structure

```bash
user-authentication-system/
│
├── app.py                  # Main Flask application file
├── config.py               # Configuration file for database URI and secret key
├── auth.py                 # authentication routes
├── models.py               # SQLAlchemy models for database tables
├── routes.py               # Flask routes for handling HTTP requests
│
├── static/                 # Folder containing static assets (CSS, JS, images)
│   ├── css/
│   ├── js/
│   ├── images/
│   └── profile_pic/
│
├── templates/           # Folder containing HTML templates
│   ├── auth/
|   |    ├── login.html        # HTML template for user login
|   |    └── register.html     # HTML template for user registration
|   |
|   ├── base.html           # Base HTML template with common layout
│   ├── index.html          # Homepage HTML template
│   ├── profile.html        # HTML template for user profile
│   └── ...
│
├── venv/
└── README.md               # Project README file
```

## Installation

  
1. Create virtual environment and activate (Optional):
- For Creating environment
   ```bash
   python -m venv venv  
   ```
- For Activating environment
   ```bash
   venv/Scripts/Activate  
   ```


2. Clone the repository:
   ```bash
   git clone https://github.com/deepraj31/flaskAuthProject.git
   ```


3. Change directory to project directory:
   ```bash
   cd flaskAuthProject
   ```

    
4. Install Required packages:
   ```bash
   pip install -r requirements.txt
   ```


- **Make sure you have a database**
- **Change the database URI and NAME accordingly in config.py**  *** **IMPORTANT** ***
  ```bash
   MYSQL_URI = 'mysql://username:password@host:port/DATABASE_NAME.db'
   ```

   
5. Run Project:
   ```bash
   python app.py
   ```
   
**After running the app, visit http://localhost:5000 to use and**
