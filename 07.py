import mysql.connector

mydb = mysql.connector.connect(
host = '127.0.0.1',
user='root',
password= '')

if not mydb:
    print('Not Connected.')
    
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS demo1')
