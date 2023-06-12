# Import the 'SQLAlchemy' class from the 'flask_sqlalchemy' module
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the 'SQLAlchemy' class
db = SQLAlchemy()

# Define a model class named 'Reptile'
class Reptile(db.Model):
    # Set the name of the database table associated with this model
    __tablename__ = 'reptiles'

    # Define the 'id' column as an integer primary key
    id = db.Column(db.Integer, primary_key=True)

    # Define the 'common_name' column as a string with a maximum length of 100 characters
    common_name = db.Column(db.String(100))

    # Define the 'scientific_name' column as a string with a maximum length of 100 characters
    scientific_name = db.Column(db.String(100))

    # Define the 'conservation_status' column as a string with a maximum length of 100 characters
    conservation_status = db.Column(db.String(100))

    # Define the 'native_habitat' column as a string with a maximum length of 200 characters
    native_habitat = db.Column(db.String(200))

    # Define the 'fun_fact' column with type of text
    fun_fact = db.Column(db.Text)

