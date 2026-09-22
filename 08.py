import mysql.connector

mydb = mysql.connector.connect(
host = '127.0.0.1',
user='root',
password= '',
database='demo1'
)

if not mydb:
    print('Not Connected.')
    
mycursor = mydb.cursor()
mycursor.execute('CREATE table IF NOT EXISTS demo1 (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))')
