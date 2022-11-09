import tkinter
from actor import insertActor
from staff import insertStaff
import sv_ttk

# create a simple window with a button, if button clicked, execute the insertActor() function
window = tkinter.Tk()
window.title("Inserir na tabela 'actor'")
window.geometry("500x200")


def abreActor():
    insertActor()


def abreStaff():
    insertStaff()


insert_actor = tkinter.Button(
    window,
    text="Tabela 'actor'",
    command=abreActor
)
insert_actor.grid(column=0, row=0)
insert_actor.config(height=4, width=18)

insert_staff = tkinter.Button(
    window,
    text="Tabela 'staff'",
    command=abreStaff
)
insert_staff.grid(column=1, row=0)
insert_staff.config(height=4, width=18)


window.mainloop()
