#Lauren Pehlivanian
#SoftDev1 pd9
#18 -- Average
#2019-10-11

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute("DROP TABLE IF EXISTS stu_avg")
# just needed for one time drop
# c.execute("DROP TABLE IF EXISTS roster")
# c.execute("DROP TABLE IF EXISTS gradebook")
c.execute("CREATE TABLE stu_avg (id INTEGER, name TEXT, avg FLOAT)")

cmd = """
    SELECT name, students.id, mark
    FROM students, courses
    WHERE students.id = courses.id;
"""

c.execute(cmd)

# This creates an array of tuples
c2 = c.fetchall()
#print(c2)

curID = c2[0][1]
sum = 0
num = 0
for i in range(len(c2)):
    # if you are done with this student
    if curID != c2[i][1]:
        #upcate curID to be current one (now diff)
        curID = c2[i][1]
        #compute avg
        avg = sum/num
        #reset sum and num vars
        #since we won't add current again, needsto be added now
        sum = c2[i][2]
        num = 1
        #add data to the TABLE
        name = c2[i-1][0]
        id = str(c2[i-1][1])
        cmd = "INSERT INTO stu_avg VALUES ("+id+", '"+name+"',"+str(avg)+")"
        print("Name: "+name+"\tID: "+id+"\tAverage: "+str(avg))
        c.execute(cmd)
    else:
        sum = sum + c2[i][2]
        num = num + 1



# c.execute(cmd)


#print(c.fetchall())

db.commit()
db.close()
