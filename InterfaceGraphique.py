from tkinter import *
from convertervrai import * 
from FaraanSupvrai import *
import sys  
import os
from numpy import *


def restart_program():
    python=sys.executable
    os.execl(python, python,* sys.argv)

window=Tk()
window.title("Venin")
canvas=Canvas(window,height=510,width=510,bg="white")
canvas.grid(row=0,column=0)


def couleur(p):
    c = ((1-p)*255)
    return rvbhex(c)


def draw(x):
    for column in range (502):
        for ligne in range (502):
            canvas.create_rectangle(x*column,x+ligne*x,2*x+x*column,x*ligne,fill="white", outline = "black")

draw(10) 

#canvas.create_oval(-70,-70,580, 580,width=138,outline="grey85" )


#variable


def propagation(x,y,p):
    
    x1, y1, x2, y2 = convertisseur_coord(x,y)
    canvas.create_rectangle(x1, y1, x2, y2, fill =couleur(p)) 

def prop(i, mat):
    x , y, z = shape(mat)
    for ligne in range (y):
        for colonne in range (z):
            propagation(ligne, colonne, mat[i, colonne, ligne])
    



def donnee(val):
    mat = launch(51,25,25,2,80)
    variable = mat[int(val)]

    prop(int(val), mat)
    canvas.create_oval(0,0,510,510,width=1,outline="black")



Button(window,text="Restart",command=restart_program, bg ="#990000") .grid(row=1,column=0)
glisseur = Scale(window,bg ="#990000", orient='horizontal',command=donnee, from_=0, to = 80, length=600) .grid(row=2, column=0)
venin_glisseur = Scale(window,bg ="#990000", orient='horizontal', from_=0, to = 10, resolution = 0.1, length=200) .grid(row=3, column=0, sticky=W)
anticoag_glisseur = Scale(window,bg ="#990000", orient='horizontal', from_=0, to = 10, resolution = 0.1, length=200) .grid(row=4, column=0, sticky=W)


window.mainloop()
