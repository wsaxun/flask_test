from . import api
from .views import *

api.add_resource(MySource1, 'ha/', 'source/')
api.add_resource(MySource2, 'source/<name>')

