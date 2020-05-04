from flask import request
from createUser import createNewUser
from flask_restful import Resource

class newUser(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        print(username, password)
        res = createNewUser(username, password)
        return res