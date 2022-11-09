import tkinter
import mysql.connector

def insertStore():

    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="root",
        database="sakila"
    )

    mycursor = mydb.cursor()