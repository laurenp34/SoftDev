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
                occupdict[row[0]] = float(row[1])                  #add the occupation as the key and the percentage as the value to the dictionary occupdict
                line_count += 1                                 #increase line count

    return occupdict
    ##print(occupdict)

##CREATE ARRAY WITH 1000 ELEMENTS, OCCUPATION PROPORTIONAL TO PERCENTAGES
def genArray(occupdict):
    occuparray = []

    for key in occupdict.keys():
        for i in range(int(occupdict[key]*10)):
            occuparray.append(occupdict[key])
    return occuparray
##print(len(occuparray))

##CHOOSE INDEX OF ARRAY RANDOMLY
def chooseOccupation(occuparray):
    return occuparray[random.randint(len(occuparray))]

def main():
    occupdict = genDict('occupations.csv')
    occuparray = genArray(occupdict)
    occ = chooseOccupation(occuparray)
    print(occ)
    return occ

main()
