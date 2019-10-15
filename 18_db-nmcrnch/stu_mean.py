# Team Bacon - Kevin Cai and Lauren Pehlivanian
# SoftDev1 pd9
# K18 -Average
# Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"
COURSE_FILE = "courses.csv";
STUDENT_FILE = "students.csv";

DEMO_NAME = "tiesto"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
def setup():
    c.execute("DROP TABLE IF EXISTS courses")
    c.execute("DROP TABLE IF EXISTS students")
    c.execute("DROP TABLE IF EXISTS stu_avg")
def loadStudents():
    with open(STUDENT_FILE, newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         test = "CREATE TABLE students (name TEXT,age INTEGER, id INTEGER);"
         c.execute(test)
         for row in reader:
             #test = "INSERT INTO students VALUES (?, ?, ?)"
             #+ str(row["name"])+"," + str(row["age"]) + "," + str(row["id"],) + ");"
             c.execute("INSERT INTO students VALUES (?, ?, ?);", (row["name"], row["age"], row["id"]))
def loadCourses():
    with open(COURSE_FILE, newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          #headers = next(reader)
          #print(headers)
          test = "CREATE TABLE courses (code TEXT,mark INTEGER, id INTEGER);"
          c.execute(test)
          for row in reader:
              #test = "INSERT INTO courses VALUES ("+ str(row["code"], ) + str(row["mark"], ) + str(row["id"],) + ");"
              c.execute("INSERT INTO courses VALUES (?, ?, ?);", (row["code"], row["mark"], row["id"]))
def setupAvgs():
    c.execute("CREATE TABLE stu_avg (avg DECIMAL, id INTEGER);")
    c.execute("SELECT id FROM students;")
    tmp = c.fetchall()
    for i in tmp:
        addAvg(lookupStudentAvg(i[0]),i[0])
def addAvg(avg, id):
    c.execute("INSERT INTO stu_avg VALUES (?, ?);", (avg, id))
def lookupStudentGrades(id):
    c.execute("SELECT code,mark FROM courses WHERE id = "+str(id)+";")
    return c.fetchall()
def lookupStudentName(id):
    c.execute("SELECT name FROM students WHERE id = "+str(id))
    return c.fetchall()[0][0]
def lookupStudentid(name):
    c.execute("SELECT id FROM students WHERE name = \""+name+"\";")
    return c.fetchall()[0][0]
def printStudentGrades(id):
    print("Grades for "+lookupStudentName(id)+" (ID "+str(id)+"):\n\n\t" +str(lookupStudentGrades(id))+"\n")
def printStudentGradesByName(name):
    printStudentGrades(lookupStudentid(name))
def lookupStudentAvg(id):
    tmp = lookupStudentGrades(id)
    count = 0
    sum = 0.0
    for i in tmp:
        count += 1
        sum += i[1]
    return sum/count
def addToCourse(code,mark,id):
    c.execute("INSERT INTO courses VALUES (?, ?, ?);", (code,mark,id))
def printStudentData(id):
    printStudentGrades(id);
    print("\tOverall avg:" +str(lookupStudentAvg(id)) +"\n")
def printAllStudentData():
    c.execute("SELECT id FROM students;")
    tmp = c.fetchall()
    #iterate though ID column to print all student data
    for i in tmp:
        printStudentData(i[0])
#==========================================================
setup()
loadStudents()
loadCourses()
printAllStudentData()
print("______________________________________________\n")
id = lookupStudentid(DEMO_NAME)
printStudentData(id)
print("add softdev grade of 100 for "+DEMO_NAME+"\n")
addToCourse("softdev", 100,id)
printStudentData(id)
setupAvgs()
print("avgs:\n")
c.execute("SELECT * FROM stu_avg ;")
print(c.fetchall())
db.commit() #save changes
db.close()  #close database#Clyde "Thluffy" Sinclair
