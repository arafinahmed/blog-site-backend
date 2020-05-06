from findingUser import connect, connectClose
def userProfile(authorid):
    try:
        connection, cursor = connect()
        create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
        cursor.execute(create_table)            
        create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
        cursor.execute(create_table)
        
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (authorid,))
        user = result.fetchone()

        if user:
            query = "SELECT * FROM allposts WHERE authorid=? ORDER BY postid DESC"
            res = cursor.execute(query, (authorid,))
            rows = res.fetchall()
            response = {user[1]:[]}
            for row in rows:
                response[user[1]].append({"postid":row[0], "post": row[1], "authorid":row[2]})
            connectClose(connection)
            return [response, 200]
        else:
            connectClose(connection)
            return [{"message":"user not found"}, 404]
    except:
        return [{"message":"internal server error"}, 500]

def singlePost(postid):
    try:
        connection, cursor = connect()
        create_table = "CREATE TABLE IF NOT EXISTS allposts (postid INTEGER PRIMARY KEY, post text, authorid INTEGER)"
        cursor.execute(create_table)      
        query = "SELECT * FROM allposts WHERE postid=?"
        result = cursor.execute(query, (postid,))
        postRes = result.fetchone()      
        if postRes:
            postid = postRes[0]
            post = postRes[1]
            authorid = postRes[2]
            query = "SELECT * FROM users WHERE id=?"
            result = cursor.execute(query, (authorid,))
            res = result.fetchone()
            connectClose(connection)
            username = res[1]
            response = {"postid":postid, "post":post, "username": username, "authorid":authorid}
            return [response, 200]
        else:
            connectClose(connection)
            return [{"message": "post not found"}, 404]
    except:
        return [{"message": "code crash"}, 500]