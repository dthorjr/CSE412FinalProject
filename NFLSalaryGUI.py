# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 01:47:52 2022

@author: lbere
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *

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
teamTab = ttk.Frame(tabControl)
positionTab = ttk.Frame(tabControl)
coachTab = ttk.Frame(tabControl)
mascotTab = ttk.Frame(tabControl)

tabControl.add(mainTab, text = 'Home')
tabControl.add(teamTab, text = 'Teams')
tabControl.add(positionTab, text = 'Positions')
tabControl.add(coachTab, text = 'Coaches')
tabControl.add(mascotTab, text = 'Mascots')
tabControl.pack(expand = 1, fill = 'both')
#header.pack()
#header.grid(column = 11, row = 0)

#def playersClick():
#header = tk.Label(mainTab, text = 'NFL Salaries', fg = 'white', bg = 'black')
#header.pack()
ttk.Label(mainTab, text = 'CSE412 Group 8', font = ('Arial', 25)).pack()
ttk.Label(mainTab, text = '').pack()
ttk.Label(mainTab, text = 'Darin Thornton').pack()
ttk.Label(mainTab, text = 'Jacob Nootens').pack()
ttk.Label(mainTab, text = 'Lauren Beresford').pack()

#playerBtn = tk.Button(mainTab, text = 'Players')
#playerBtn.grid(column = 0, row = 12)
#coachBtn = tk.Button(mainTab, text = 'Coaches')
#coachBtn.grid(column = 8, row = 12)
#mascotBtn = tk.Button(mainTab, text = 'Mascots')
#mascotBtn.grid(column = 16, row = 12)
#playerBtn.pack()
#coachBtn.pack()
#mascotBtn.pack()

###team tab
teams = ['Ravens','Bills','Panthers','Bears','Bengals','Browns',
         'Cowboys','Broncos','Lions','Packers','Texans','Colts',
         'Jaguars','Chiefs','Raiders','Chargers','Rams','Dolphins',
         'Vikings','Patriots','Saints','Giants','Jets','Eagles',
         'Steelers','49ers','Seahawks','Buccaneers','Titans','Commanders']
avgSalaries = [420,69,420,69,420,69,420,69,420,69,420,69,420,69,420,69,
               420,69,420,69,420,69,420,69,420,69,420,69,420,69]
colors = ['red', 'yellow', 'black', 'blue', 'orange', 'cyan', 'green']

figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, teamTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(teams))
ax.bar(x_pos, avgSalaries, color = colors)
ax.set_title('Average Salaries by Team')

ttk.Label(teamTab, text = '').pack()
ttk.Label(teamTab, text = 'Select a Team').pack()
selected = StringVar()
selected.set('Chiefs')
drop = OptionMenu(teamTab, selected, *teams)
drop.pack()

###graph fun
mascotNames = ['Bacon','Avocado','Lettuce','Egg']
mascotSalary = [420,69,12,62]


figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, mascotTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(mascotNames))
ax.bar(x_pos, mascotSalary, color = colors)
ax.set_title('Mascot Salaries')


window.mainloop()