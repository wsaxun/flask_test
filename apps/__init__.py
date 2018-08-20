from flask import Flask
from apps.login import loginBlue
from apps.core import coreBlue
from config import config


def create_app(env):
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config.get(env))

    app.register_blueprint(loginBlue, url_prefix='/login/')  # 前缀
    app.register_blueprint(coreBlue, url_prefix='/core/')
    return app


if __name__ == '__main__':
    app = create_app('defalult')
