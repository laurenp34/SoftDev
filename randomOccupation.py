import csv

##CREATE OCCUPATIONS DICTIONARY WITH PERCENTAGES AS VALUES:

occupdict = {}                                          #instantiate occupdict as a dictionary

with open('occupations.csv') as occupations:
    reader = csv.reader(occupations, delimiter=',')     #read in the file and break it up using ',' as the delimiter
    line_count = 0                                      #define the line count
    for row in reader:                                  #for each row do this
        if line_count > 0 and row[0] != 'Total':        #if the line is not the first or last line do this
            occupdict[row[0]] = row[1]                  #add the occupation as the key and the percentage as the value to the dictionary occupdict
        line_count += 1                                 #increase line count

print(occupdict)
