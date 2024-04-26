from tkinter import *

def menu():
    root = Tk()
    root.title("Restaurant")
    root.resizable(False, False)


    frame= Frame(root,width=480,height=420)
    frame.pack()
    frame.config(cursor="pirate")


    #Bucle de la aplicación
    root.mainloop()

