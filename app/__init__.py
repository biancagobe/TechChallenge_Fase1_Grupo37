from flask import Flask
from flask_caching import Cache
from flasgger import Swagger
from flask_httpauth import HTTPTokenAuth

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize extensions
cache = Cache(app)
auth = HTTPTokenAuth(scheme='Bearer')

# Configure Swagger
swagger = Swagger(app)

# Import utilities (after 'auth' is defined)
from app.utils import auth as auth_utils

# Import routes (after 'app' is fully initialized)
from app.routes import auth_routes, scrape_routes
