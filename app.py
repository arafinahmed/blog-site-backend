from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from auth import auth_handle, id_handle
from operation import newUser, myPost

app = Flask(__name__)
app.secret_key = "thisisasecretkey"
api = Api(app)

jwt = JWT(app, auth_handle, id_handle)
   
api.add_resource(myPost, '/post')
api.add_resource(newUser, '/register')
if __name__ == '__main__':
    app.run(port=8888, debug=True)