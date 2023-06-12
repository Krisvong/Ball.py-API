from flask import Blueprint, redirect, request
from . import models 

# Create a Blueprint instance for the 'reptile' blueprint
bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

# Define a route for handling the index page
@bp.route('/', methods=['GET', 'POST'])
def index(): 
    # POST method
    if request.method == 'POST':
        # Create a new reptile object with data from the form
        new_reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )
        
        # Add the new reptile to the database
        models.db.session.add(new_reptile)
        models.db.session.commit()
        
        # Redirect to the index page
        return redirect('/reptiles')
    
    # GET method
    # Retrieve all reptiles from the database
    found_reptiles = models.Reptile.query.all()

    # Create an empty dictionary with an empty list value
    reptile_dict = {'reptiles': []}

    # Loop through all reptiles and append their data to the list in the dictionary
    for reptile in found_reptiles:
        reptile_dict["reptiles"].append({
            'common_name': reptile.common_name,
            'scientific_name': reptile.scientific_name,
            'conservation_status': reptile.conservation_status,
            'native_habitat': reptile.native_habitat,
            'fun_fact': reptile.fun_fact
        })

    # Return the dictionary as the JSON response
    return reptile_dict

# Define a route for showing information about a specific reptile
@bp.route('/<int:id>')
def show(id): 
    # Find the reptile by ID
    reptile = models.Reptile.query.filter_by(id=id).first()

    # Create a dictionary with the reptile's information
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.scientific_name,
        'conservation_status': reptile.conservation_status,
        'native_habitat': reptile.native_habitat,
        'fun_fact': reptile.fun_fact
    }
    
    # Return the dictionary as the JSON response
    return reptile_dict
