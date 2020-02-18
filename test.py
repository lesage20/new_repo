#!/usr/bin/env python3
# coding:utf-8

import tkinter
import sys

#creation de l'interface primaire
app = Tk()
#ce code est bizarre qui fait ça??
app.config(bg="#550000")
app.geometry("800x600")

#fonctions
def quit():
  sys.exit("messagebox.showinfo(sys.platform"))
  
  
# creation des widgets
label = tkinter.Label(app, text="Hello I'am the sage", font="Arial 14 bold")
label1 = tkinter.Label(app, text="I am Kevin Elysée ", font="Arial 14 bold")
bouton=Button(fenetre, text="Fermer", command=quit)

#Affichage des widgets
label.pack(padx=10, pady=10, ipady=5)
label1.pack(padx=10, pady=10, ipady=5)
bouton.pack()

#boucle principale
app.mainloop()
