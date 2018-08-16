from flask import Blueprint

loginBlue = Blueprint('loginName', __name__, template_folder='templates')

from .login import *
from .urls import *
