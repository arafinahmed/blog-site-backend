import sqlite3
from findingUser import connect, connectClose

def createNewUser(username, password):
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