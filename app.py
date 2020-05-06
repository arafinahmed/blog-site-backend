from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from auth import auth_handle, id_handle
from operation import newUser, myPost, profile, detailsPost

app = Flask(__name__)
app.secret_key = "thisisasecretkey"
api = Api(app)

jwt = JWT(app, auth_handle, id_handle)
   
api.add_resource(myPost, '/post')
api.add_resource(newUser, '/register')
api.add_resource(profile, "/profile/<string:authorid>")
api.add_resource(detailsPost, "/post/<string:postid>")

if __name__ == '__main__':
    app.run(port=8888, debug=True)