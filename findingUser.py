import sqlite3

def connect():
    connection = sqlite3.connect('test3.db')
    cursor = connection.cursor()
    return [connection, cursor]
def connectClose(connection):
    connection.commit()
    connection.close()

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(self, name):
        connection, cursor = connect()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connectClose(connection)

        if row:
            return User(row[0], row[1], row[2])
        else:
            return None
    @classmethod
    def find_by_userid(self, userid):
        connection, cursor = connect()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (userid,))
        row = result.fetchone()
        connectClose(connection)
        if row:
            return User(row[0], row[1], row[2])
        else:
            return None


        

