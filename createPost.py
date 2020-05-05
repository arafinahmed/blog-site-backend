import sqlite3
from findingUser import connect, connectClose

def newPost(post, authorid):
    try:
        connection, cursor = connect('posts.db')  
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
    connection, cursor = connect('posts.db')  
    create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
    cursor.execute(create_table)
    update_query = "UPDATE allposts set post=? WHERE postid=? AND authorid=?"
    update = (post, postid, authorid)
    cursor.execute(update_query, update)
    connectClose(connection)
    return {"message":"updated"}

