from flask import Flask
from apps.login import loginBlue
from apps.core import coreBlue
from apps.api import api_bp
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env):
    apps = Flask(__name__, template_folder='../templates',
                 static_folder='../static')
    apps.config.from_object(config.get(env))
    db.init_app(apps)
    apps.register_blueprint(loginBlue, url_prefix='/login/')  # 前缀
    apps.register_blueprint(coreBlue, url_prefix='/core/')
    apps.register_blueprint(api_bp, url_prefix='/api/')
    print(apps.url_map)
    return apps


if __name__ == '__main__':
    app = create_app('defalult')
