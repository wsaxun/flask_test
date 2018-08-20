from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

api_bp = Blueprint('apiName', __name__)
CORS(api_bp, supports_credentials=True)
api = Api(api_bp)


from .urls import *
from .views import *
