
from Tkinter import *
from converter import * 
import time
import sys  
import os


def restart_program():
    python=sys.executable
    os.execl(python, python,* sys.argv)

window=Tk()
canvas=Canvas(window,height=500,width=500,bg="white")
canvas.grid(row=0,column=1)


def couleur(p):
    c = ((1-p)*255)
    return rvbhex(c)


def draw(x):
    for column in range (501):
        for ligne in range (501):
            canvas.create_rectangle(x*column,x+ligne*x,2*x+x*column,x*ligne,fill=couleur(0),outline="white")

draw(10) 

canvas.create_oval(-55,-55,555, 555,width=110,outline="grey85" )
canvas.create_oval(0,0,500,500,width=1,outline="red")

def propagation(x,y,p):
    x1, y1, x2, y2 = convertisseur_coord(x,y)

    canvas.create_rectangle(x1, y1, x2, y2, fill =couleur(p), outline = "white" ) 

propagation(24,24,1)
propagation(24,25,0.8)
propagation(24,26,0.5)
propagation(25,24,1)
propagation(25,25,0.8)
propagation(25,26,0.5)
propagation(26,24,1)
propagation(26,25,0.8)
propagation(26,26,0.5)
propagation(27,24,1)
propagation(27,25,0.8)
propagation(27,26,0.5)


def donnee():
    print(5)

print(couleur(0.44))


Button(window,text="Morsure",command=donnee) .grid(row=0,column=0)
Button(window,text="Restart",command=restart_program) .grid(row=1,column=0)

window.mainloop()