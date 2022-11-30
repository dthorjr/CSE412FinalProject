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
conn = psycopg2.connect(
database="salaries_NFL",
user="new",
password="admin",
host="localhost",
port="5432"
)
db = conn.cursor()

window = tk.Tk()
window.title('Welcome to NFL Salary Database!')
window.geometry('1280x720')

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


ttk.Label(teamTab, text = 'NFL Teams Page', font = ('Arial', 25)).pack()
ttk.Label(teamTab, text = '').pack()

#team average graph
figure = plt.Figure(figsize=(6,6), dpi=100)
ax = figure.add_subplot(111)
ax.tick_params(axis='x', rotation=90)
chart_type = FigureCanvasTkAgg(figure, teamTab)
chart_type.get_tk_widget().pack()
#x_pos = np.arange(len(teams))
ax.bar(teams, avgSalaries, color = teamColors)
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

listTeamFirstName = [] 
listTeamLastName = []
listTeamSalary = []

T = Text(window, height = 50, width = 50)
T.pack()
#print table of players
def team_changed(event): 
    listTeamFirstName = [] 
    listTeamLastName = []
    listTeamSalary = []
    T.delete(0.0,'end')
    ttk.Label(teamTab, text = 'Current Team is ' + str(drop.get())).pack()
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
    
    for i in range(10):
        T.insert(tk.END, listTeamFirstName[i])
        T.insert(tk.END, '\t \t')
        T.insert(tk.END, listTeamLastName[i])
        T.insert(tk.END, '\t \t')
        T.insert(tk.END, listTeamSalary[i])
        T.insert(tk.END, '\n')
        
drop.bind('<<ComboboxSelected>>', team_changed)


###positions tab
ttk.Label(positionTab, text = 'NFL Positions Page', font = ('Arial', 25)).pack()
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
#x_pos = np.arange(len(positions))
ax.bar(position, avgPosSalary, color = positionColors)
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

listPositionFirstName = [] 
listPositionLastName = []
listPositionSalary = []
#print table of players by position

def pos_changed(event):
    listPositionFirstName = [] 
    listPositionLastName = []
    listPositionSalary = []
    
    ttk.Label(positionTab, text = 'Current Position is ' + str(dropPos.get())).pack()
    currentPos = str(dropPos.get())
    
    T.delete(0.0,'end')
    
    db.execute("SELECT Player.firstName, Player.lastName, Player.salary FROM Player, Position WHERE Position.positionid = Player.positionid AND Position.positionname = \'{0}\' ORDER BY Player.salary DESC".format(currentPos))

    for Player in db:
        firstName, lastName, salary = Player
        listPositionFirstName.append(firstName)
        listPositionLastName.append(lastName)
        listPositionSalary.append(salary)
        
    T.insert(tk.END, 'First Name:')
    T.insert(tk.END, '\t\t')
    T.insert(tk.END, 'Last Name:')
    T.insert(tk.END, '\t\t')
    T.insert(tk.END, 'Salary:')
    T.insert(tk.END, '\n')
    
    for i in range(10):
        T.insert(tk.END, listPositionFirstName[i])
        T.insert(tk.END, '\t \t')
        T.insert(tk.END, listPositionLastName[i])
        T.insert(tk.END, '\t \t')
        T.insert(tk.END, listPositionSalary[i])
        T.insert(tk.END, '\n')
        
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
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, coachTab)
chart_type.get_tk_widget().pack()
#x_pos = np.arange(len(coaches))
ax.bar(listCoachLastName, listCoachSalary, color = teamColors)
ax.set_title('Salaries for NFL Coaches')


###mascot tab
ttk.Label(mascotTab, text = 'NFL Mascots Page', font = ('Arial', 25)).pack()
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
ax.bar(x_pos, mascotSalary, color = teamColors)
ax.set_title('Mascot Salaries')


window.mainloop()
