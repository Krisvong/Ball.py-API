# Factory

from flask import Flask, redirect
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    # Configuration and other setup can be done here

    # database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ardilla0103!@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import the 'models' module
    from . import models
    # Initialize the database with the Flask 'app' instance
    models.db.init_app(app)
    # Create an instance of the 'Migrate' class, passing the Flask 'app' instance and the database instance ('models.db')
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index():
        return redirect('/reptiles')

    # register reptiles blueprint
    from . import reptile
    app.register_blueprint(reptile.bp)

    return app
