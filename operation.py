from flask import request
from createUser import createNewUser
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity
from createPost import newPost, updatePost

class newUser(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data["username"]
            password = data["password"]
            res, code = createNewUser(username, password)
            return res, code
        except:
            return {"message":"bad request"}, 400

class myPost(Resource):
    
    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            post = data["post"]
            message, code = newPost(post, current_identity.id)
            return message, code
        except:
            return {"message":"bad request"}, 400
    
    @jwt_required()
    def put(self):
        try:
            data = request.get_json()
            postid = int(data['postid'])
            post = data["post"]
            return updatePost(postid, post, current_identity.id)
            
        except:
            return {"message": "bad request"}, 400
       

