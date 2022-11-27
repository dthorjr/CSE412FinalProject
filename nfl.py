import psycopg2
import tkinter as tk
from tkinter import *

w = tk.Tk()
w.geometry("400x250")
conn = psycopg2.connect(
        database="salaries_NFL",
        user="new",
        password="admin",
        host="localhost",
        port="5432"
        )

db = conn.cursor()

db.execute("SELECT Mascot.salary, Mascot.name, Team.name FROM Mascot, Team WHERE Team.teamid = Mascot.teamid ORDER BY Mascot.salary DESC")

i=0
for Mascot in db:
    for j in range(len(Mascot)):
        e = Entry(w,width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, Mascot[j])
    i=i+1
w.mainloop()
