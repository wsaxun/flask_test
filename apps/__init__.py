from flask import Flask
from apps.login import loginBlue
from apps.core import coreBlue
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .core import models as coreModels  # 让flask-migrate发现model，否则无法创建表结构
from .login import models as loginModels


def create_app(env):
    apps = Flask(__name__, template_folder='../templates',
                 static_folder='../static')
    apps.config.from_object(config.get(env))
    db.init_app(apps)
    apps.register_blueprint(loginBlue, url_prefix='/login/')  # 前缀
    apps.register_blueprint(coreBlue, url_prefix='/core/')
    return apps


if __name__ == '__main__':
    app = create_app('defalult')
