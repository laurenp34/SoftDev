import csv
import random

##CREATE OCCUPATIONS DICTIONARY WITH PERCENTAGES AS VALUES:
def genDict(filename):
    occupdict = {}                                          #instantiate occupdict as a dictionary

    with open(filename) as occupations:
        reader = csv.reader(occupations, delimiter=',')     #read in the file and break it up using ',' as the delimiter
        line_count = 0                                      #define the line count
        for row in reader:                                  #for each row do this
            if line_count > 0 and row[0] != 'Total':        #if the line is not the first or last line do this
                occupdict[row[0]] = float(row[1])           #add the occupation as the key and the percentage as the value to the dictionary occupdict
            line_count += 1
    return occupdict
    ##print(occupdict)

##CREATE ARRAY WITH 1000 ELEMENTS, OCCUPATION PROPORTIONAL TO PERCENTAGES
def genArray(occupdict):
    occuparray = []

    for key in occupdict.keys():
        for i in range(int(occupdict[key]*10)):
            occuparray.append(key)
    return occuparray
#print(len(occuparray))

##CHOOSE INDEX OF ARRAY RANDOMLY
def chooseOccupation(occuparray):
    return occuparray[random.randint(0,len(occuparray))]

def laurenMain():
    occupdict = genDict('occupations.csv')
    #print(occupdict)
    occuparray = genArray(occupdict)
    #print(occuparray)
    occ = chooseOccupation(occuparray)
    #print(occ)
    return occ

#   STEP 1 - generate a dictionary, using the CSV as input

def dictGenerate(filename):

    myDict = {}  #  initializing empty dictionary

    #   reading through CSV file

    with open('occupations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line = 0
        for row in csv_reader:
            if line > 0 and row[0] != 'Total':
                myDict[row[0]] = float(row[1])
            line = line + 1

    #   FOR TESTING PURPOSES --> print(myDict)
    return myDict



#   STEP 2 - generate a random number, and pick a specific field from the dictionary using said number

def occuPick(dict):
    pickedNum = float(random.randrange(0, 998)) / 10    #   picking a random number between 0 and 99.8, to be picked from the dictionary

    total = 0.0 #   Note: var total is updated as we move through the dictionary keys

    for entry in dict:
        total = total + dict[entry]     #   update total to represent the range currently occupied
        if pickedNum < total:   #   if random number chosen is in the range between the previous entry and the current entry, output
            print(pickedNum, '\t', entry)   #   print entry
            return entry    #   output entry
            break



#   Note: main() goes here; this is what is output to the Flask app
def main():
    q = dictGenerate('occupations.csv')
    return occuPick(q)

#   Calling on main()
main()
