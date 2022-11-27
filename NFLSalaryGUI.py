# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:47:52 2022

@author: lbere
"""

import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

window = tk.Tk()
window.title('Welcome to NFL Salary Database!')
window.geometry('350x200')

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
header.pack()
playerBtn.pack()
coachBtn.pack()
mascotBtn.pack()
window.mainloop()