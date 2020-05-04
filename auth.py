from findingUser import User

user = 'arafin'
passw = 'hello'

def auth_handle(username, password):
    user = User.find_by_username(username)    
    if user and user.password == password:
        return user

def id_handle(payload):
    userid = payload['identity']
    return User.find_by_userid(userid)
