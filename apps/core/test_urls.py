from . import coreBlue
from . import MyView2, MyView1

coreBlue.add_url_rule('/', view_func=MyView1.as_view('hello'))
coreBlue.add_url_rule('/name/<username>', view_func=MyView2.as_view('name'))

