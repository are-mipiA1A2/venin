
from Tkinter import *
from converter import * 
import time
import sys  
import os


def restart_program():
    python=sys.executable
    os.execl(python, python,* sys.argv)




window=Tk()
canvas=Canvas(window,height=490,width=490,bg="white")
canvas.grid(row=0,column=0)


def couleur(p):
    c = ((1-p)*255)
    return rvbhex(c)


def draw(x):
    for column in range (500):
        for ligne in range (500):
            canvas.create_rectangle(x*column,x+ligne*x,2*x+x*column,x*ligne,fill=couleur(1),outline="white")

draw(10) 

liste = [0.4,1,0.99,0.45,1,0.47,0.48,0.49,1]
def propagation(liste):
    for i in range(len(liste)):
        canvas.create_rectangle(240,240,250,250,fill=couleur(liste[i]),outline="white")
propagation(liste)

canvas.create_oval(-25,-25,515, 515,width=140,outline="white" )
canvas.create_oval(45,45,445,445,width=3,outline="red")


print(couleur(0.44))

def donnee():
    print(5)
Button(window,text="Morsure",command=donnee) .grid(row=1,column=1)
Button(window,text="Restart",command=restart_program) .grid(row=0,column=1)

window.mainloop()