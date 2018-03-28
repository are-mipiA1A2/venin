
from Tkinter import *
from converter import * 
import time
import sys  
import os
from numpy import *


def restart_program():
    python=sys.executable
    os.execl(python, python,* sys.argv)

window=Tk()
canvas=Canvas(window,height=510,width=510,bg="white")
canvas.grid(row=0,column=1)


def couleur(p):
    c = ((1-p)*255)
    return rvbhex(c)


def draw(x):
    for column in range (502):
        for ligne in range (502):
            canvas.create_rectangle(x*column,x+ligne*x,2*x+x*column,x*ligne,fill="white", outline = "black")

draw(10) 

canvas.create_oval(-70,-70,580, 580,width=138,outline="grey85" )
canvas.create_oval(0,0,510,510,width=1,outline="black")

#variable
mat = array([[[1, 0.02245242],
        [0.05411948, 0.10433879]],

       [[0.02142567, 1],
        [0.06447764, 0.03263258]],

       [[0.02934682, 0.07481326],
        [1, 0.09996509]],

       [[0.016496  , 0.09931502],
        [0.06480892, 1]]])


def propagation(x,y,p):
    
    x1, y1, x2, y2 = convertisseur_coord(x,y)
    canvas.create_rectangle(x1, y1, x2, y2, fill =couleur(p)) 

def prop(mat):
    x , y, z = shape(mat)
    for i in range (x):

        for ligne in range (y):
            for colonne in range (z):
                propagation(ligne, colonne, mat[i, ligne, colonne])
    
prop(mat)

#propagation(25,25,1)
#propagation(25,50,1)
#propagation(25,0,1)
#propagation(0,25,1)
#propagation(50,25,1)


def donnee():
    

    print(couleur(0.44))


Button(window,text="Morsure",command=donnee) .grid(row=0,column=0)
Button(window,text="Restart",command=restart_program) .grid(row=1,column=0)

window.mainloop()