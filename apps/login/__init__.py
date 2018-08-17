from flask import Blueprint

loginBlue = Blueprint('loginName', __name__)

from .login import *
from .urls import *
