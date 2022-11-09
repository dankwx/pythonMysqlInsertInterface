import tkinter
import mysql.connector
from datetime import datetime
import sv_ttk


def insertActor():

    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="root",
        database="sakila"
    )

    mycursor = mydb.cursor()

    # insert into table 'actor' into the values 'actor_id', 'first_name', 'last_name', 'last_update', but make a window with winker and insert the values

    def insert():
        actor_id = actor_id_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        last_update = last_update_entry.get()
        sql = "INSERT INTO actor (actor_id, first_name, last_name, last_update) VALUES (%s, %s, %s, %s)"
        val = (actor_id, first_name, last_name, last_update)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    window = tkinter.Tk()
    window.title("Inserir na tabela 'actor'")
    window.geometry("500x200")

    actor_id_label = tkinter.Label(window, text="actor_id")
    actor_id_label.grid(column=0, row=1)

    first_name_label = tkinter.Label(window, text="first_name")
    first_name_label.grid(column=0, row=2)

    last_name_label = tkinter.Label(window, text="last_name")
    last_name_label.grid(column=0, row=3)

    last_update_label = tkinter.Label(window, text="last_update")
    last_update_label.grid(column=0, row=4)

    actor_id_entry = tkinter.Entry(window, width=30)
    actor_id_entry.grid(column=1, row=1)

    def increase():
        actor_id = int(actor_id_entry.get())
        actor_id += 1
        actor_id_entry.delete(0, tkinter.END)
        actor_id_entry.insert(0, str(actor_id))

    def decrease():
        actor_id = int(actor_id_entry.get())
        actor_id -= 1
        actor_id_entry.delete(0, tkinter.END)
        actor_id_entry.insert(0, str(actor_id))

    increase_button = tkinter.Button(
        window, text="        +        ", command=increase)
    increase_button.grid(column=2, row=1)
    decrease_button = tkinter.Button(
        window, text="        -        ", command=decrease)
    decrease_button.grid(column=3, row=1)

    def random_name():
        # get a array of brazilian names from https://gist.github.com/augustohp/2c59ceb96e195ea375abadb311637e7f
        names = ["Ana", "Bia", "Carla", "Dani", "Eva", "Fernanda", "Gabi", "Heloisa", "Iara", "Julia",
                 "Kauana", "Lara", "Maria", "Nina", "Olivia", "Paula", "Querida", "Rafaela", "Sabrina", "Tatiana"]
        import random
        name = random.choice(names)
        first_name_entry.delete(0, tkinter.END)
        first_name_entry.insert(0, name)

    first_name_entry = tkinter.Entry(window, width=30)
    first_name_entry.grid(column=1, row=2)
    random_name_button = tkinter.Button(
        window, text="Adicionar", command=random_name)
    random_name_button.grid(column=2, row=2)

    def random_last_name():
        last_names = ["Alves", "Borges", "Carvalho", "Dias", "Elias", "Ferreira", "Gomes", "Hernandes", "Ivan", "Jorge",
                      "Kauana", "Lima", "Machado", "Nunes", "Oliveira", "Pereira", "Queiroz", "Rocha", "Santos", "Tavares"]
        import random
        last_name = random.choice(last_names)
        last_name_entry.delete(0, tkinter.END)
        last_name_entry.insert(0, last_name)

    last_name_entry = tkinter.Entry(window, width=30)
    last_name_entry.grid(column=1, row=3)
    random_last_name_button = tkinter.Button(
        window, text="Adicionar", command=random_last_name)
    random_last_name_button.grid(column=2, row=3)

    last_update_entry = tkinter.Entry(window, width=30)
    last_update_entry.grid(column=1, row=4)

    insert_button = tkinter.Button(window, text="Insert", command=insert)
    insert_button.grid(column=0, row=5)

    # styles
    actor_id_entry.focus()
    insert_button.grid(pady=10)
    last_update_entry.insert(0, datetime.now())
    actor_id_label.config(font=("Arial", 11))
    first_name_label.config(font=("Arial", 11))
    last_name_label.config(font=("Arial", 11))
    last_update_label.config(font=("Arial", 11))
    insert_button.config(font=("Arial", 11))
    actor_id_entry.config(font=("Arial", 11))
    first_name_entry.config(font=("Arial", 11))
    last_name_entry.config(font=("Arial", 11))
    last_update_entry.config(font=("Arial", 11))

    actor_id_entry.delete(0, 'end')
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    last_update_entry.delete(0, 'end')

    # search the last actor_id on the table 'actor' and add 1 to the next actor_id
    mycursor.execute(
        "SELECT actor_id FROM actor ORDER BY actor_id DESC LIMIT 1")
    myresult = mycursor.fetchall()
    for x in myresult:
        actor_id_entry.insert(0, str(x[0] + 1))

    # display the current hora in the top of the window, and it updates every second
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    label = tkinter.Label(window, text=current_time)

    def tick():
        hora = datetime.now()
        hora = hora.strftime("%H:%M:%S")
        label.config(text=hora)
        label.after(1000, tick)
        # do a simple  style
        label.config(font=("Arial", 11))

    tick()

    def atualizar():
        tick()
        last_update_entry.delete(0, tkinter.END)
        last_update_entry.insert(0, datetime.now())

    label = tkinter.Label(window, text="")
    label.grid(column=3, row=4)
    atualizar_button = tkinter.Button(
        window, text="Adicionar", command=atualizar)
    atualizar_button.grid(column=2, row=4)

    sv_ttk.set_theme('dark')
    window.mainloop()


# insertActor()
