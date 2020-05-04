from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from auth import auth_handle, id_handle
from createUser import createNewUser

app = Flask(__name__)
app.secret_key = "thisisasecretkey"
api = Api(app)

jwt = JWT(app, auth_handle, id_handle)


class test(Resource):
    def get(self):
        return {"message": "Working"}

class newUser(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        print(username, password)
        res = createNewUser(username, password)
        return res


    
api.add_resource(test, '/')
api.add_resource(newUser, '/register')
if __name__ == '__main__':
    app.run(port=8888, debug=True)