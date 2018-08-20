from datetime import datetime
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from flask import request

resource_fields = {
    'task':   fields.String,
    'uri':    fields.String
}


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


class MySource1(Resource):
    @marshal_with(resource_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int,
                            help='Rate to charge for this resource')
        abort(404, message='404')
        return TodoDao(todo_id='my_todo', task='Remember the milk')


class MySource2(Resource):
    def get(self, name):
        return {'name': name}
