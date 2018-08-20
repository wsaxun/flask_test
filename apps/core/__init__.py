from flask import Blueprint


coreBlue = Blueprint('coreName', __name__)
from .core import *
from .urls import *