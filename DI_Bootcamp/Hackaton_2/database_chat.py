import sqlite3 as sl

def run_query(query):
    connection = sl.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def fetch_query(query):
    connection = sl.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

def signup_server_db(username, ip_address):
    try:
        query = f"INSERT INTO user (username, ip_add) VALUES ('{username}', '{ip_address}')"
        run_query(query)
        # welcome_msg = f"Welcome {username}"
        # print(welcome_msg)
    except:
        error = 'This username already exists'
        print(error)

def signin_server_db(username):
    query = f"SELECT username FROM user WHERE username == '{username}'"
    results = fetch_query(query)
    if results == []:
        error = "This username doesn't exist"
        print(error)
        return False
    return results

def message_server_db(sender, receiver, message):
    pass