#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

# from sample import hello
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    """
    api: /api/HelloWorld
    restful 接口调用测试
    """

    def get(self):
        print('Hello world of RESTful api!')
        return {'hello': 'zzdeworld'}

    def post(self):
        mydata = request.form['data']
        return {'hello': mydata}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)