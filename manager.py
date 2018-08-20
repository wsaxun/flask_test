from apps import create_app
from flask_script import Manager, Shell, Server

app = create_app('default')
manager = Manager(app)


@app.shell_context_processor  # 进入shell之后，可以直接使用app, xums对象
def test():
    return dict(app=app, xums=[])


@manager.command
def hello(name):
    print('hello {0}'.format(name))


manager.add_command('runserver',
                    Server(host='0.0.0.0', port=5000, use_reloader=True,
                           use_debugger=True))
manager.add_command('shell', Shell(make_context=test))

if __name__ == '__main__':
    manager.run()
