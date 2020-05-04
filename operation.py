from flask import request
from createUser import createNewUser
from flask_restful import Resource
from flask_jwt import jwt_required

class newUser(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        print(username, password)
        res, code = createNewUser(username, password)
        return res, code

class test(Resource):
    @jwt_required()
    def get(self):
        return {"message":"this is working bro"}