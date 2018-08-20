from flask.views import View


class MyView3(View):
    def dispatch_request(self):  # 继承View必须实现dispatch_request函数
        return 'hahah'
