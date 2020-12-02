import os
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()
app = FlaskAPI(__name__, instance_relative_config=True)
ma = Marshmallow(app)
CORS(app)



def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'dffbjkjfjnsfjfamf_nefjkhe'
    app.secret_key = os.environ.get('SECRET')
    db.init_app(app)
    jwt = JWTManager(app)

    # Import all the Blueprints and register them

    # Register blueprint

    

    
    return app
