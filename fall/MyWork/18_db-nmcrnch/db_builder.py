#Lauren Pehlivanian
#SoftDev1 pd9
#17 -- No Trouble
#2019-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

#REMOVE ROSTER (from when it was created before)
c.execute("DROP TABLE IF EXISTS students")
c.execute("DROP TABLE IF EXISTS courses")

#create table with fields from both csv files
# only create table if already doesn't exist (prevents duplicate error)
# command = "CREATE TABLE IF NOT EXISTS roster (id INTEGER, name TEXT, age INTEGER, code TEXT, mark INTEGER)"          # test SQL stmt in sqlite3 shell, save as string

command = "CREATE TABLE IF NOT EXISTS courses (id INTEGER, code TEXT, mark INTEGER)"
c.execute(command)
command = "CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, age INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

# print("---------------------")

# print("---------------------")

with open('courses.csv') as courcsv:
    coursesDict = csv.DictReader(courcsv)
    for row in coursesDict:
        # insert statement, fills in fields in this dict, othwersie null.
        # cmd = "INSERT INTO roster VALUES("+row['id']+", NULL, NULL, '"+row['code']+"', "+row['mark']+")"
        cmd = "INSERT INTO courses VALUES("+row['id']+", '"+row['code']+"', "+row['mark']+")"
        c.execute(cmd)
        #print(row)

with open('students.csv') as stucsv:
     studentsDict = csv.DictReader(stucsv)
     for row in studentsDict:
         #print(row)
         # update age and name info for all rows(each row- based on id)
         # cmd = "UPDATE roster SET name='"+row['name']+"', age="+row['age']+" WHERE id="+row['id']
         #print(cmd)
         cmd = "INSERT INTO students VALUES("+row['id']+", '"+row['name']+"', "+row['age']+")"
         c.execute(cmd)

# c.execute("INSERT INTO roster VALUES(2, 'LAUREN', NULL, NULL, NULL)") TEST SMTH

#create table with fields from both csv files
# command = "CREATE TABLE IF NOT EXISTS roster (id INTEGER, name TEXT, age INTEGER, code TEXT, mark INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

#populate roster with values from students dict acc to field
# for row in studentsDict:
#     c.execute("INSERT INTO roster INT NULL")
#     for key in row:
#         cmd = "INSERT "

#print roster

#==========================================================

db.commit() #save changes

# c.execute("SELECT * FROM roster")
#print(c.fetchall())

db.close()  #close database
