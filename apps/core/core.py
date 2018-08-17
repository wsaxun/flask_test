from flask.views import MethodView
from flask import url_for, redirect, render_template
from ..core import coreBlue

class MyView1(MethodView):
    def get(self):
        return render_template('hello.html')


class MyView2(MethodView):
    def get(self, username='name'):
        # return username
        return redirect(url_for('coreName.hello'))  # 视图函数名为‘hello’

@coreBlue.route('/')
def index():
    return render_template('hello.html')
