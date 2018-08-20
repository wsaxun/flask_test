from flask.views import MethodView
from flask import url_for, redirect, render_template


class MyView1(MethodView):
    def get(self):
        return render_template('hello.html')


class MyView2(MethodView):
    def get(self, username='name'):
        return redirect(url_for('coreName.hello'))  # 视图函数名为‘hello’
