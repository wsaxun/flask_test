from flask import Blueprint

coreBlue = Blueprint('coreName', __name__, template_folder='templates')

from .core import *
from .urls import *
