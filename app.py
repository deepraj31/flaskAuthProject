from flask import Flask
from models import db
from config import MYSQL_URI, SECRET_KEY




app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI



db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()



from routes import *
from auth import *

if __name__ == '__main__':
    app.run(debug=True)