import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="root",
    database="sakila"
)

mycursor = mydb.cursor()

# delete the person with the id 9999 from the table 'actor'
sql = "DELETE FROM actor WHERE actor_id = 9993"
mycursor.execute(sql)
mydb.commit()
