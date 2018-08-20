from flask import Blueprint
from flask_cors import CORS  # 引入跨域插件

coreBlue = Blueprint('coreName', __name__)
CORS(coreBlue, supports_credentials=True)  # 对蓝图使用跨域插件
from .views import *
from .urls import *
