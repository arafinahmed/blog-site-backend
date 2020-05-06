import sqlite3
from findingUser import connect, connectClose

def postVerification(name):
    char = False
    num = False
    length = False
    for c in name:
        if c >='A' and c <='Z':
            char = True
        if c >='a' and c <='z':
            char = True
        if c >= '0' and c <= '9':
            num = True
    if len(name) > 4:
        length = True
    return((char or num) and length)


def newPost(post, authorid):
    try:
        verify = postVerification(post)
        if verify == False:
            return [{"message": "invalid post"}, 400]
        connection, cursor = connect()  
        create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
        cursor.execute(create_table)
        newpost = (None,post, authorid)
        insert_query = "INSERT INTO allposts VALUES(?,?,?)"
        cursor.execute(insert_query, newpost)
        connectClose(connection)
        return [{"message": "post successful"}, 200]
    except:
        return [{"message":"something error"}, 500]

def updatePost(postid, post, authorid):
    try:
        verify = postVerification(post)
        if verify == False:
            return [{"message": "invalid post"}, 400]
        connection, cursor = connect()  
        create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
        cursor.execute(create_table)
        
        query = "SELECT * FROM allposts WHERE postid=? AND authorid=?"
        req = (postid, authorid)
        result = cursor.execute(query, req)
        row = result.fetchone()
        if row:
            update_query = "UPDATE allposts set post=? WHERE postid=? AND authorid=?"
            update = (post, postid, authorid)
            cursor.execute(update_query, update)
            connectClose(connection)
            return [{"message":"updated"}, 200]
        connectClose(connection)
        return [{"message": "bad request"}, 400]
    except:
        return [{"message":"something error"}, 500]


def deletePost(postid, authorid):
    try:
        connection, cursor = connect()  
        create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
        cursor.execute(create_table)
            
        query = "SELECT * FROM allposts WHERE postid=? AND authorid=?"
        req = (postid, authorid)
        result = cursor.execute(query, req)
        row = result.fetchone()

        if row:
            delete_query = "DELETE FROM allposts WHERE postid=? AND authorid=?"
            cursor.execute(delete_query, req)
            connectClose(connection)
            return [{"message":"post deleted"}, 200]
        connectClose(connection)
        return[{"message": "you are not permitted to delete"}, 400]
    except:
        return [{"message":"something error"}, 500]

def allpost():
    try:
        connection, cursor = connect()  
        create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
        cursor.execute(create_table)            
        query = "SELECT * FROM allposts ORDER BY postid DESC"
        res = cursor.execute(query)
        rows = res.fetchall()
        response = {"allposts":[]}
        for row in rows:
            response["allposts"].append({"postid":row[0], "post": row[1], "authorid":row[2]})
        connectClose(connection)
        return [response, 200]
    except:
        return [{"message":"something error"}, 500]



    



    

