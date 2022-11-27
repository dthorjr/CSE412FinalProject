# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:47:52 2022

@author: lbere
"""
import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter import *


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
###########################
#Database retrieval code
db_window = tk.Tk()
conn = psycopg2.connect(
        database="salaries_NFL",
        user="new",
        password="admin",
        host="localhost",
        port="5432"
        )
db = conn.cursor()

x = 'Broncos'
y = 'Patriots'
db.execute("SELECT Mascot.salary, Mascot.name, Team.name FROM Mascot, Team WHERE (Team.name = \'{0}\' OR Team.name = \'{1}\') AND Team.teamid = Mascot.teamid ORDER BY Mascot.salary DESC".format(x,y))

i=0
for Mascot in db:
    for j in range(len(Mascot)):
        e = Entry(db_window,width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, Mascot[j])
    i=i+1
###########################
window = tk.Tk()
window.attributes('-fullscreen',True)
window.title('Welcome to NFL Salary Database!')
window.geometry('1280x720')

tabControl = ttk.Notebook(window)
mainTab = ttk.Frame(tabControl)
playerTab = ttk.Frame(tabControl)
coachTab = ttk.Frame(tabControl)
mascotTab = ttk.Frame(tabControl)

tabControl.add(mainTab, text = 'Home')
tabControl.add(playerTab, text = 'Players')
tabControl.add(coachTab, text = 'Coaches')
tabControl.add(mascotTab, text = 'Mascots')
tabControl.pack(expand = 1, fill = 'both')
#header.pack()
#header.grid(column = 11, row = 0)

#def playersClick():
header = tk.Label(mainTab, text = 'NFL Salaries', fg = 'white', bg = 'black')

playerBtn = tk.Button(mainTab, text = 'Players')
#playerBtn.grid(column = 0, row = 12)
coachBtn = tk.Button(mainTab, text = 'Coaches')
#coachBtn.grid(column = 8, row = 12)
mascotBtn = tk.Button(mainTab, text = 'Mascots')
#mascotBtn.grid(column = 16, row = 12)
closeBtn = tk.Button(mainTab, text = 'Close', command=window.destroy)
header.pack()
playerBtn.pack()
coachBtn.pack()
mascotBtn.pack()
closeBtn.pack()
window.mainloop()