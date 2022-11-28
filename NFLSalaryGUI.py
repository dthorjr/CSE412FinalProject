# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:47:52 2022

@author: lbere
"""

import tkinter as tk
from tkinter import ttk

import pandas as pd
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = tk.Tk()
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
header.pack()
playerBtn.pack()
coachBtn.pack()
mascotBtn.pack()

###graph fun
mascotNames = ['Bacon','Avocado','Lettuce','Egg']
mascotSalary = [420,69,12,62]
c = ['red', 'yellow', 'black', 'blue', 'orange']

figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, window)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(mascotNames))
ax.bar(x_pos, mascotSalary, color = c)
ax.set_title('Mascot Salaries')


window.mainloop()