import datetime
import random
import tkinter
from tkinter import ttk
from click import style
import mysql.connector


def insertStaff():
    import sv_ttk
    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="root",
        database="sakila"
    )

    mycursor = mydb.cursor()

    def insert():
        staff_id = staff_id_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        address_id = address_id_entry.get()
        picture = picture_entry.get()
        email = email_entry.get()
        store_id = store_id_entry.get()
        active = active_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        last_update = last_update_entry.get()
        sql = "INSERT INTO staff (staff_id, first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (staff_id, first_name, last_name, address_id, picture,
               email, store_id, active, username, password, last_update)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    window = tkinter.Tk()
    window.title("Inserir na tabela 'staff'")
    window.geometry("500x280")
    sv_ttk.set_theme('dark')

    staff_id_label = tkinter.Label(window, text="staff_id")
    staff_id_label.grid(column=0, row=1)

    first_name_label = tkinter.Label(window, text="first_name")
    first_name_label.grid(column=0, row=2)

    last_name_label = tkinter.Label(window, text="last_name")
    last_name_label.grid(column=0, row=3)

    address_id_label = tkinter.Label(window, text="address_id")
    address_id_label.grid(column=0, row=4)

    picture_label = tkinter.Label(window, text="picture")
    picture_label.grid(column=0, row=5)

    email_label = tkinter.Label(window, text="email")
    email_label.grid(column=0, row=6)

    store_id_label = tkinter.Label(window, text="store_id")
    store_id_label.grid(column=0, row=7)

    active_label = tkinter.Label(window, text="active")
    active_label.grid(column=0, row=8)

    username_label = tkinter.Label(window, text="username")
    username_label.grid(column=0, row=9)

    password_label = tkinter.Label(window, text="password")
    password_label.grid(column=0, row=10)

    last_update_label = tkinter.Label(window, text="last_update")
    last_update_label.grid(column=0, row=11)

    staff_id_entry = tkinter.Entry(window, width=30)
    staff_id_entry.grid(column=1, row=1)

    # get the highest staff_id and add 1 to it
    mycursor.execute("SELECT MAX(staff_id) FROM staff")
    myresult = mycursor.fetchall()
    staff_id_entry.insert(0, myresult[0][0] + 1)

    # make the staff_id field read-only
    staff_id_entry.config(state="readonly")

    first_name_entry = tkinter.Entry(window, width=30)
    first_name_entry.grid(column=1, row=2)

    last_name_entry = tkinter.Entry(window, width=30)
    last_name_entry.grid(column=1, row=3)

    address_id_entry = tkinter.Entry(window, width=30)
    address_id_entry.grid(column=1, row=4)

    picture_entry = tkinter.Entry(window, width=30)
    picture_entry.grid(column=1, row=5)

    email_entry = tkinter.Entry(window, width=30)
    email_entry.grid(column=1, row=6)

    store_id_entry = tkinter.Entry(window, width=30)
    store_id_entry.grid(column=1, row=7)

    # get all store_id from table 'store', and show it on a select tag, then get the selected value into store_id entry
    mycursor.execute("SELECT store_id FROM store")
    myresult = mycursor.fetchall()
    store_id_list = []
    for x in myresult:
        store_id_list.append(x)
    store_id_select = ttk.Combobox(window, values=store_id_list)
    store_id_select.grid(column=2, row=7)
    store_id_select.current(0)
    store_id_select.bind("<<ComboboxSelected>>", lambda e: store_id_entry.insert(
        0, store_id_select.get()))

    active_entry = tkinter.Entry(window, width=30)
    active_entry.grid(column=1, row=8)

    # make a select tag with 2 values, '0 - False' and '1 - True', then get the selected integer and insert it into active entry
    active_select = ttk.Combobox(window, values=[
        '0 - False', '1 - True'])
    active_select.grid(column=2, row=8)
    active_select.current(0)
    active_select.bind("<<ComboboxSelected>>", lambda e: active_entry.insert(
        0, active_select.get()[0]))

    # every time the user selects a value from the select tag, clear the entry  and insert the selected value
    def clear_active_entry(event):
        active_entry.delete(0, "end")
        active_entry.insert(0, active_select.get()[0])
    active_select.bind("<<ComboboxSelected>>", clear_active_entry)

    username_entry = tkinter.Entry(window, width=30)
    username_entry.grid(column=1, row=9)

    password_entry = tkinter.Entry(window, width=30)
    password_entry.grid(column=1, row=10)
    # make the password entry invisible
    password_entry.config(show="*")

    last_update_entry = tkinter.Entry(window, width=30)
    last_update_entry.grid(column=1, row=11)

    insert_button = tkinter.Button(window, text="Inserir", command=insert)
    insert_button.grid(column=1, row=12)

    # set picture to null
    picture_entry.insert(0, "null")

    # make a button 'Inserir' to insert the data on last_update entry

    def insertTime():
        last_update_entry.delete(0, 'end')
        last_update_entry.insert(0, datetime.datetime.now())

    insert_time_button = tkinter.Button(
        window, text="Inserir", command=insertTime)
    insert_time_button.grid(column=2, row=11)

    # make a button 'Inserir' to insert a random first name on first_name entry

    def insertFirstName():
        first_names = ["John", "Mary", "Peter", "Paul",
                       "George", "Ringo", "Paula", "Felipe", "Jonathan"]
        first_name_entry.delete(0, 'end')
        first_name_entry.insert(0, random.choice(first_names))

    insert_first_name_button = tkinter.Button(
        window, text="Inserir", command=insertFirstName)
    insert_first_name_button.grid(column=2, row=2)

    # make a button 'Inserir' to insert a random last name on last_name entry

    def insertLastName():
        last_names = ["Smith", "Jones", "Williams", "Brown",
                      "Davis", "Miller", "Wilson", "Moore", "Taylor"]
        last_name_entry.delete(0, 'end')
        last_name_entry.insert(0, random.choice(last_names))

    insert_last_name_button = tkinter.Button(
        window, text="Inserir", command=insertLastName)
    insert_last_name_button.grid(column=2, row=3)

    # make a button 'Inserir' to insert a random email on email entry, but get the value inside first_name and last_name entries, like: 'jonathan.paul + @email.com'

    def insertEmail():
        email_entry.delete(0, 'end')
        email_entry.insert(0, first_name_entry.get().lower() + "." +
                           last_name_entry.get().lower() + "@email.com")

    insert_email_button = tkinter.Button(
        window, text="Inserir", command=insertEmail)
    insert_email_button.grid(column=2, row=6)

    # make a button 'Inserir' to insert a random username on username entry, but get the value inside first_name + random 2 numbers

    def insertUsername():
        username_entry.delete(0, 'end')
        username_entry.insert(0, first_name_entry.get().lower() + "." +
                              str(random.randint(10, 99)))

    insert_username_button = tkinter.Button(
        window, text="Inserir", command=insertUsername)
    insert_username_button.grid(column=2, row=9)

    window.mainloop()


# insertStaff()
