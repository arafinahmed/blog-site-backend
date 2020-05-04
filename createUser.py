import sqlite3
from findingUser import connect, connectClose

def nameVerification(name):
    for c in name:
        if c >='A' and c <='Z':
            return False
        if c >='a' and c <='z':
            return False
    return True
def passwordVerification(password):
    if password == False:
        return True
    if len(password) <4:
        return True
    return False


def createNewUser(username, password):
    checkname = nameVerification(username)
    if checkname:
        return {"message": "invalid name"}
    checkpassword = passwordVerification(password)
    if checkpassword:
        return {"password": "password length must be 4"}
    

    connection, cursor = connect()    

    create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)
    
    query = "SELECT * FROM users WHERE username=?"
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
        connectClose(connection)
        return {"message": "username already exist, try new username"}

    user = (None,username, password)
    insert_query = "INSERT INTO users VALUES(?,?,?)"
    cursor.execute(insert_query, user)

    connectClose(connection)
    return {"message": "user created"}