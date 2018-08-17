from flask import Flask
from apps.login import loginBlue
# from apps.core import coreBlue
from config import config


def create_app(env):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config.get(env))
    config.get(env).init_app(app)

    # app.config.update(SERVER_NAME='0.0.0.0')

    from apps.core import coreBlue

    app.register_blueprint(loginBlue, url_prefix='/login/')  # 前缀
    app.register_blueprint(coreBlue, url_prefix='/core/')
    print(app.url_map)

    # app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run()
    return app

if __name__ == '__main__':
    app = create_app('default')
    app.run()
