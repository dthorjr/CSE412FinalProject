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
ttk.Label(mainTab, text = '').pack()
ttk.Label(mainTab, text = 'Welcome to the NFL Salary Database').pack()
ttk.Label(mainTab, text = 'Where you can view the differences in pay between').pack()
ttk.Label(mainTab, text = 'Teams, positions, coaches, and mascots!').pack()


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
selectedTeam = StringVar()
selectedTeam.set('Cardinals')
drop = ttk.Combobox(teamTab, textvariable = selectedTeam)
drop['values'] = teams
drop['state'] = 'readonly'
drop.pack()
currentTeam = ''

#print table of players
def team_changed(event):
    ttk.Label(teamTab, text = 'Current Team is ' + str(drop.get())).pack()
    currentTeam = str(drop.get())
    #print(db.execute("SELECT Player.firstName, Player.lastName, Player.salary 
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

#positions graph
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, positionTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(positions))
ax.bar(x_pos, avgPosSalaries, color = colors)
ax.set_title('Average Salaries by Position')

#positions dropdown menu
ttk.Label(positionTab, text = '').pack()
ttk.Label(positionTab, text = 'Select a Position').pack()
selected = StringVar()
selected.set('Quarterback')
dropPos = ttk.Combobox(positionTab, textvariable = selected)
dropPos['values'] = positions
dropPos['state'] = 'readonly'
dropPos.pack()

#print table of players by position
def pos_changed(event):
    ttk.Label(positionTab, text = 'Current Position is ' + str(dropPos.get())).pack()
    currentPos = str(dropPos.get())
    #print(db.execute("SELECT Player.firstName, Player.lastName, Player.salary 
    #FROM Player, Position 
    #WHERE Position.positionid = Player.positionid AND Position.name = currentPos
    #ORDER BY Player.salary DESC"))
dropPos.bind('<<ComboboxSelected>>', pos_changed)


###coaches tab
ttk.Label(coachTab, text = 'Coaches Page', font = ('Arial', 25)).pack()
ttk.Label(coachTab, text = '').pack()

#data grab
coaches = ['poop','poopPants']
coachSalaries = ['69','420']

#coach graph
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, coachTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(coaches))
ax.bar(x_pos, coachSalaries, color = colors)
ax.set_title('Salaries for NFL Coaches')


###mascot tab
ttk.Label(mascotTab, text = 'Mascots Page', font = ('Arial', 25)).pack()
ttk.Label(mascotTab, text = '').pack()

#data grab
mascotNames = ['Bacon','Avocado','Lettuce','Egg']
mascotSalary = [420,69,12,62]

#mascot graph
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, mascotTab)
chart_type.get_tk_widget().pack()
x_pos = np.arange(len(mascotNames))
ax.bar(x_pos, mascotSalary, color = colors)
ax.set_title('Mascot Salaries')


window.mainloop()