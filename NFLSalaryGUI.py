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

import math

#connect to database
conn = psycopg2.connect(
database="salaries_NFL",
user="new",
password="admin",
host="localhost",
port="5432"
)
db = conn.cursor()

#create main window using tkinter
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

#instantiation
teamColors = [] 
teams = []
avgSalaries = [] 

db.execute("SELECT Team.name, Team.color1, AVG(Player.salary) FROM Team, Player WHERE Team.teamid = Player.teamid GROUP BY Team.name, Team.color1 ORDER BY AVG(Player.salary) DESC")

for Player in db:
    teamNames, teamColor, teamSalary = Player
    teams.append(teamNames)
    teamColors.append(teamColor)
    avgSalaries.append(teamSalary)

position = []
avgPosSalary = []
positionColors = ['red', 'green', 'blue', 'yellow', 'magenta']
db.execute("SELECT Position.positionname, Position.abbr, AVG(Player.salary) FROM Position, Player WHERE Player.positionid = Position.positionid GROUP BY Position.positionname, Position.abbr ORDER BY AVG(Player.salary) DESC")

for Position in db:
    positionName, abr, positionAvg = Position
    position.append(positionName)
    avgPosSalary.append(positionAvg)


###team tab

ttk.Label(teamTab, text = 'NFL Teams Page', font = ('Arial', 25)).pack()
ttk.Label(teamTab, text = '').pack()

#team average graph
figure = plt.Figure(figsize=(6,6), dpi=100)
ax = figure.add_subplot(111)
ax.tick_params(axis = 'x', rotation = 90)
chart_type = FigureCanvasTkAgg(figure, teamTab)
chart_type.get_tk_widget().pack(side = LEFT)
#x_pos = np.arange(len(teams))
ax.bar(teams, avgSalaries, color = teamColors)
ax.set_title('Average Salaries by Team')

#query and calculate average salary
db.execute("SELECT avg(Player.salary + Coach.salary + Mascot.salary) FROM Player, Coach, Mascot")
for Salary in db:
    avgSalary = Salary[0]
avgSalary = math.trunc(avgSalary)

ttk.Label(teamTab, text = 'The average salary across all teams is: $' + str(avgSalary)).pack()

#team dropdown menu
ttk.Label(teamTab, text = '').pack()
ttk.Label(teamTab, text = 'Select a Team').pack()
selectedTeam = StringVar()
selectedTeam.set('                --------')
drop = ttk.Combobox(teamTab, textvariable = selectedTeam)
drop['values'] = teams
drop['state'] = 'readonly'
drop.pack()
currentTeam = ''

listTeamFirstName = [] 
listTeamLastName = []
listTeamSalary = []

scroll = Scrollbar(teamTab, orient = 'vertical')
T = Text(teamTab, width = 50, yscrollcommand = scroll.set)

#print table of players
def team_changed(event):
    listTeamFirstName = [] 
    listTeamLastName = []
    listTeamSalary = []
    T.delete(0.0,'end')
    
    #ttk.Label(teamTab, text = 'Current Team is ' + str(drop.get())).pack()
    currentTeam = str(drop.get())
    
    db.execute("SELECT Player.firstName, Player.lastName, Player.salary FROM Player, Team  WHERE Team.teamid = Player.teamid AND Team.name = \'{0}\' ORDER BY Player.salary DESC".format(currentTeam))
    for Player in db:
        firstName, lastName, salary = Player
        listTeamFirstName.append(firstName)
        listTeamLastName.append(lastName)
        listTeamSalary.append(salary)
        
    T.insert(tk.END, 'First Name:')
    T.insert(tk.END, '\t\t')
    T.insert(tk.END, 'Last Name:')
    T.insert(tk.END, '\t\t')
    T.insert(tk.END, 'Salary:')
    T.insert(tk.END, '\n')
    
    for i in range(len(listTeamFirstName)):
        T.insert(tk.END, listTeamFirstName[i])
        T.insert(tk.END, '\t \t')
        T.insert(tk.END, listTeamLastName[i])
        T.insert(tk.END, '\t \t')
        T.insert(tk.END, listTeamSalary[i])
        T.insert(tk.END, '\n')
        
    scroll.config(command = T.yview)
    T.pack()

drop.bind('<<ComboboxSelected>>', team_changed)


###positions tab
ttk.Label(positionTab, text = 'NFL Positions Page', font = ('Arial', 25)).pack()
ttk.Label(positionTab, text = '').pack()

#positions graph
figure = plt.Figure(figsize=(6,6), dpi=100)
ax = figure.add_subplot(111)
ax.tick_params(axis = 'x', rotation = 90)
chart_type = FigureCanvasTkAgg(figure, positionTab)
chart_type.get_tk_widget().pack(side = LEFT)
#x_pos = np.arange(len(positions))
ax.bar(position, avgPosSalary, color = positionColors)
ax.set_title('Average Salaries by Position')

#query and calculate average salary
db.execute("SELECT AVG(Player.salary) FROM Player")
for Salary in db:
    avgSalary2 = Salary[0]
avgSalary2 = math.trunc(avgSalary2)

ttk.Label(positionTab, text = 'The average salary across all positions is: $' + str(avgSalary2)).pack()

#positions dropdown menu
ttk.Label(positionTab, text = '').pack()
ttk.Label(positionTab, text = 'Select a Position').pack()
selected = StringVar()
selected.set('                 --------')
dropPos = ttk.Combobox(positionTab, textvariable = selected)
dropPos['values'] = position
dropPos['state'] = 'readonly'
dropPos.pack()

listPositionFirstName = [] 
listPositionLastName = []
listPositionSalary = []

scroll2 = Scrollbar(positionTab, orient = 'vertical')
T2 = Text(positionTab, width = 50, yscrollcommand = scroll2.set)

#print table of players by position
def pos_changed(event):
    listPositionFirstName = [] 
    listPositionLastName = []
    listPositionSalary = []
    
    #ttk.Label(positionTab, text = 'Current Position is ' + str(dropPos.get())).pack()
    currentPos = str(dropPos.get())
    
    T2.delete(0.0,'end')
    
    db.execute("SELECT Player.firstName, Player.lastName, Player.salary FROM Player, Position WHERE Position.positionid = Player.positionid AND Position.positionname = \'{0}\' ORDER BY Player.salary DESC".format(currentPos))

    for Player in db:
        firstName, lastName, salary = Player
        listPositionFirstName.append(firstName)
        listPositionLastName.append(lastName)
        listPositionSalary.append(salary)
        
    T2.insert(tk.END, 'First Name:')
    T2.insert(tk.END, '\t\t')
    T2.insert(tk.END, 'Last Name:')
    T2.insert(tk.END, '\t\t')
    T2.insert(tk.END, 'Salary:')
    T2.insert(tk.END, '\n')
    
    for i in range(len(listPositionFirstName)):
        T2.insert(tk.END, listPositionFirstName[i])
        T2.insert(tk.END, '\t \t')
        T2.insert(tk.END, listPositionLastName[i])
        T2.insert(tk.END, '\t \t')
        T2.insert(tk.END, listPositionSalary[i])
        T2.insert(tk.END, '\n')
        
    scroll2.config(command = T2.yview)
    T2.pack()
        
dropPos.bind('<<ComboboxSelected>>', pos_changed)


###coaches tab
ttk.Label(coachTab, text = 'NFL Coaches Page', font = ('Arial', 25)).pack()
ttk.Label(coachTab, text = '').pack()

#data grab
listCoachLastName = []
listCoachSalary = []
db.execute("SELECT coach.lastname,coach.salary FROM coach")
for Coach in db:
    lastName, salary = Coach
    listCoachLastName.append(lastName)
    listCoachSalary.append(salary)

#coach graph
figure = plt.Figure(figsize=(6,6), dpi=100)
ax = figure.add_subplot(111)
ax.tick_params(axis = 'x', rotation = 90)
chart_type = FigureCanvasTkAgg(figure, coachTab)
chart_type.get_tk_widget().pack(side = LEFT)
#x_pos = np.arange(len(coaches))
ax.bar(listCoachLastName, listCoachSalary, color = teamColors)
ax.set_title('Salaries for NFL Coaches')

db.execute("SELECT AVG(Coach.salary) FROM Coach")
for Salary in db:
    avgSalary3 = Salary[0]
avgSalary3 = math.trunc(avgSalary3)

#query and calculate average salary
ttk.Label(coachTab, text = 'The average salary for NFL coaches is: $' + str(avgSalary3)).pack()

scroll3 = Scrollbar(positionTab, orient = 'vertical')
T3 = Text(coachTab, width = 70, yscrollcommand = scroll3.set)

db.execute("SELECT Coach.salary, Coach.FirstName, Coach.LastName, Team.name FROM Coach, Team WHERE Team.teamid = Coach.teamid ORDER BY Coach.salary DESC")
listCoachSalaries = []
listCoachFirstName = []
listCoachLastName = []
listCoachTeamName = []
for Coach in db:
    salary, firstName, lastName, teamName = Coach
    listCoachSalaries.append(salary)
    listCoachFirstName.append(firstName)
    listCoachLastName.append(lastName)
    listCoachTeamName.append(teamName)
        
T3.insert(tk.END, 'Team Name:')
T3.insert(tk.END, '\t\t')
T3.insert(tk.END, 'First Name:')
T3.insert(tk.END, '\t\t')
T3.insert(tk.END, 'Last Name:')
T3.insert(tk.END, '\t\t')
T3.insert(tk.END, 'Salary:')
T3.insert(tk.END, '\n')
    
for i in range(len(listCoachTeamName)):
    T3.insert(tk.END, listCoachTeamName[i])
    T3.insert(tk.END, '\t \t')
    T3.insert(tk.END, listCoachFirstName[i])
    T3.insert(tk.END, '\t \t')
    T3.insert(tk.END, listCoachLastName[i])
    T3.insert(tk.END, '\t \t')
    T3.insert(tk.END, listCoachSalaries[i])
    T3.insert(tk.END, '\n')
        
scroll3.config(command = T3.yview)
T3.pack()
        

###mascot tab
ttk.Label(mascotTab, text = 'NFL Mascots Page', font = ('Arial', 25)).pack()
ttk.Label(mascotTab, text = '').pack()

#data grab
listMascotName = []
listMascotSalary = []

db.execute("SELECT Mascot.salary, Mascot.name, Team.name FROM Mascot, Team WHERE Team.teamid = Mascot.teamid ORDER BY Mascot.salary DESC")
for Mascot in db:
    salary, name, teamName = Mascot
    listMascotName.append(name)
    listMascotSalary.append(salary)

#mascot graph
figure = plt.Figure(figsize=(6,6), dpi=100)
ax = figure.add_subplot(111)
ax.tick_params(axis = 'x', rotation = 90)
chart_type = FigureCanvasTkAgg(figure, mascotTab)
chart_type.get_tk_widget().pack(side = LEFT)
#x_pos = np.arange(len(mascotNames))
ax.bar(listMascotName, listMascotSalary, color = teamColors)
ax.set_title('Mascot Salaries')

db.execute("SELECT AVG(Mascot.salary) FROM Mascot")
for Salary in db:
    avgSalary4 = Salary[0]
avgSalary4 = math.trunc(avgSalary4)

#query and calculate average salary
ttk.Label(mascotTab, text = 'The average salary for NFL mascots is: $' + str(avgSalary4)).pack()

scroll4 = Scrollbar(mascotTab, orient = 'vertical')
T4 = Text(mascotTab, width = 70, yscrollcommand = scroll4.set)

db.execute("SELECT Mascot.salary, Mascot.name, Team.name FROM Mascot, Team WHERE Team.teamid = Mascot.teamid ORDER BY Mascot.salary DESC")
listMascotSalaries = []
listMascotName = []
listMascotTeamName = []
for Mascot in db:
    salary, mascotName, teamName = Mascot
    listMascotSalaries.append(salary)
    listMascotName.append(mascotName)
    listMascotTeamName.append(teamName)
        
T4.insert(tk.END, 'Mascot Name:')
T4.insert(tk.END, '\t\t')
T4.insert(tk.END, 'Team Name:')
T4.insert(tk.END, '\t\t')
T4.insert(tk.END, 'Salary:')
T4.insert(tk.END, '\n')
    
for i in range(len(listMascotTeamName)):
    T4.insert(tk.END, listMascotName[i])
    T4.insert(tk.END, '\t \t')
    T4.insert(tk.END, listMascotTeamName[i])
    T4.insert(tk.END, '\t \t')
    T4.insert(tk.END, listMascotSalaries[i])
    T4.insert(tk.END, '\n')
        
scroll4.config(command = T4.yview)
T4.pack()


window.mainloop()
