#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api

# from sample import hello
app = Flask(__name__)
api = Api(app)


class ColdModel(Resource):
    """
    api: /api/ColdModel
    restful 接口调用测试
    """

    def get(self):
        print('This is api for humancoldmodel!')
        return {'hello': 'coldmodelcloud'}

    def post(self):
        mydata = request.form['data']
        return {'hello': mydata}


api.add_resource(ColdModel, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
