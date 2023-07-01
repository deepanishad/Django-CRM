# Install Mysql on yoour Computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345678',
    auth_plugin = 'mysql_native_password',

)

# prepare a cursor object
cursorObject = dataBase.cursor()

#create a databse

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")