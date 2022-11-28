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

import psycopg2

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

ttk.Label(mainTab, text = 'CSE412 Group 8', font = ('Arial', 25)).pack()
ttk.Label(mainTab, text = '').pack()
ttk.Label(mainTab, text = 'Darin Thornton').pack()
ttk.Label(mainTab, text = 'Jacob Nootens').pack()
ttk.Label(mainTab, text = 'Lauren Beresford').pack()


###team tab
teams = ['Cardinals','Ravens','Bills','Panthers','Bears','Bengals','Browns',
         'Cowboys','Broncos','Lions','Packers','Texans','Colts',
         'Jaguars','Chiefs','Raiders','Chargers','Rams','Dolphins',
         'Vikings','Patriots','Saints','Giants','Jets','Eagles',
         'Steelers','49ers','Seahawks','Buccaneers','Titans','Commanders']
avgSalaries = [69,420,69,420,69,420,69,420,69,420,69,420,69,420,69,420,69,
               420,69,420,69,420,69,420,69,420,69,420,69,420,69]
colors = ['red', 'yellow', 'black', 'blue', 'orange', 'cyan', 'green']

ttk.Label(teamTab, text = 'Teams Page', font = ('Arial', 25)).pack()
ttk.Label(teamTab, text = '').pack()

#team average graph
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, teamTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(teams))
ax.bar(x_pos, avgSalaries, color = colors)
ax.set_title('Average Salaries by Team')

#team dropdown menu
ttk.Label(teamTab, text = '').pack()
ttk.Label(teamTab, text = 'Select a Team').pack()
selected = StringVar()
selected.set('Cardinals')
drop = ttk.Combobox(teamTab, textvariable = selected)
drop['values'] = teams
drop['state'] = 'readonly'
drop.pack()
currentTeam = ''

#print table of players
def team_changed(event):
    ttk.Label(teamTab, text = 'Current Team is ' + str(drop.get())).pack()
    currentTeam = str(drop.get())
    #print(db.execute("SELECT Player.firstName, Mascot.lastName, Player.salary 
    #FROM Player, Team 
    #WHERE Team.teamid = Player.teamid AND Team.name = currentTeam
    #ORDER BY Player.salary DESC"))
drop.bind('<<ComboboxSelected>>', team_changed)


###positions tab
ttk.Label(positionTab, text = 'Positions Page', font = ('Arial', 25)).pack()
ttk.Label(positionTab, text = '').pack()

positions = ['Quarterback','Running Back', 'Full Back','Wide Receiver',
           'Tight End','Left Tackle','Left Guard','Center','Right Guard',
           'Right Tackle','Cornerback','Strong Safety','Free Safety',
           'Defensive End','Defensive Tackle','Outside Linebacker',
           'Inside Linebacker','Linebacker','Kicker','Punter']
avgPosSalaries = [69,420,69,420,69,420,69,420,69,420,69,420,69,420,69,420,69,
               420,69,420]

#team graph
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, positionTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(positions))
ax.bar(x_pos, avgPosSalaries, color = colors)
ax.set_title('Average Salaries by Position')

#team dropdown menu
ttk.Label(positionTab, text = '').pack()
ttk.Label(positionTab, text = 'Select a Position').pack()
selected = StringVar()
selected.set('Quarterback')
drop2 = OptionMenu(positionTab, selected, *positions)
drop2.pack()

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