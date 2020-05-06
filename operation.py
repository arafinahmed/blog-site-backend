from flask import request
from createUser import createNewUser
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity
from createPost import newPost, updatePost, deletePost, allpost
from publicPost import userProfile, singlePost

class newUser(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data["username"]
            password = data["password"]
            res, code = createNewUser(username, password)
            return res, code
        except:
            return {"message":"something error"}, 500

class myPost(Resource):

    def get(self):
        try:
            message, code = allpost()
            return message, code
        except:
            return {"message":"something error"}, 500

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            post = data["post"]
            message, code = newPost(post, current_identity.id)
            return message, code
        except:
            return {"message":"something error"}, 500
    
    @jwt_required()
    def put(self):
        try:
            data = request.get_json()
            postid = int(data['postid'])
            post = data["post"]
            message, code = updatePost(postid, post, current_identity.id)
            return message , code
            
        except:
            return {"message":"something error"}, 500
    
    @jwt_required()
    def delete(self):
        try:
            data = request.get_json()
            postid = int(data['delete'])
            message, code = deletePost(postid, current_identity.id)
            return message, code
        except:
            return {"message":"something error"}, 500


class profile(Resource):
    def get(self,authorid):
        try:
            message, code =  userProfile(int(authorid))
            return message, code
        except:
            return {"message":"something error"}, 500

class detailsPost(Resource):
    def get(self, postid):
        try:
            message, code = singlePost(int(postid))
            return message, code
        except:
            return {"message":"something error"}, 500

            

