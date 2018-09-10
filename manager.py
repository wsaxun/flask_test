import os
from apps import create_app, db
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from apps.core import models as coreModels  # 让flask-migrate发现model，否则无法创建表结构
from apps.login import models as loginModels
from apps.auth import models as authModels

app = create_app(os.getenv('FLASK_ENV', 'default'))
migrate = Migrate(app, db)
manager = Manager(app)


@app.shell_context_processor  # 进入shell之后，可以直接使用app, xums对象
def test():
    return dict(app=app, loginModels=loginModels, coreModels=coreModels)


@manager.command  # 执行hello命令是具体操作
def hello(name):
    print('hello {0}'.format(name))


manager.add_command('runserver',  # 添加命令，第一个参数命令名
                    Server(host='0.0.0.0', port=5000, use_reloader=True,
                           use_debugger=True))
manager.add_command('shell', Shell(make_context=test))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
