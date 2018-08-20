from flask import Blueprint
from flask_cors import CORS

loginBlue = Blueprint('loginName', __name__)
CORS(loginBlue, supports_credentials=True)

from .views import *
from .urls import *