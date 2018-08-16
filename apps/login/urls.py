from . import loginBlue
from . import MyView3

loginBlue.add_url_rule('/', view_func=MyView3.as_view('3view'))
