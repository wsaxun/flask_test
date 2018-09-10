from flask import Blueprint
from flask_cors import CORS

auth_blue = Blueprint('auth', __name__)
CORS(auth_blue, supports_credentials=True)


from .urls import *
from .views import *
