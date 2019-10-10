#Lauren Pehlivanian
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

with open('students.csv') as stucsv:
     studentsDict = csv.DictReader(stucsv)
     for row in studentsDict:
         print(row)
print("---------------------")
with open('courses.csv') as courcsv:
    coursesDict = csv.DictReader(courcsv)
    for row in coursesDict:
        print(row)

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
