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
mycursor.execute('insert into demo1 (name, email, password) values ("John Doe", "john.doe@example.com", "password123")')
mydb.commit()
