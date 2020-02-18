#!/usr/bin/env python3
# coding:utf-8

import tkinter

app = Tk()
#ce code est bizarre qui fait ça??


label = tkinter.Label(app, text="Hello I'am the sage", font="Arial 14 bold")
label.pack(padx=10, pady=10, ipady=5)

label = tkinter.Label(app, text="Me is Kevin", font="Arial 14 bold")
label.pack(padx=10, pady=10, ipady=5)

bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

app.mainloop()
