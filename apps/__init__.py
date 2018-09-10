from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(env):
    apps = Flask(__name__, template_folder='../templates',
                 static_folder='../static')
    apps.config.from_object(config.get(env))
    db.init_app(apps)
    login_manager.init_app(apps)
    from apps.login import loginBlue    # 放入此函数下，解决循环引用问题
    from apps.core import coreBlue
    from apps.api import api_bp
    from apps.auth import auth_blue
    apps.register_blueprint(loginBlue, url_prefix='/login/')  # 前缀
    apps.register_blueprint(coreBlue, url_prefix='/core/')
    apps.register_blueprint(api_bp, url_prefix='/api/')
    apps.register_blueprint(auth_blue, url_prefix='/auth/')
    return apps


if __name__ == '__main__':
    app = create_app('defalult')
