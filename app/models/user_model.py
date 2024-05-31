# In models/user_model.py
from config import MYSQL_CONNECTION 

def register_user(username, password):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    MYSQL_CONNECTION.commit()
    cur.close()

def authenticate_user(username, password):
    cur = MYSQL_CONNECTION.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()
    return user
