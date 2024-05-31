# MySQL configuration
MYSQL_HOST='127.0.0.1'
MYSQL_USER='root'
MYSQL_PASSWORD= 'Meghana@123'
MYSQL_DB='course_management_system'

import mysql.connector 

MYSQL_CONNECTION = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, database=MYSQL_DB)