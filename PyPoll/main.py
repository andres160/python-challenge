import csv
import os
import collections
import numpy as np

# Path to collect data from the Resources folder

pypollCSV = os.path.join( 'Resources', 'election_data1.csv')

candidate = []

with open (pypollCSV) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        candidate.append(row[2])
        voter_count = len(candidate)
        candidate_counter = collections.Counter(candidate)
        counts = dict(collections.Counter(candidate))
        candidate_percent = {k: v / len(candidate) for k,v in counts.items()}

# print to terminal

def name_the_key(dict, key):
    return key, dict[key]

mydict = candidate_percent
mydict2 = candidate_counter

print("Election Results")
print("------------------------------")
print("Total Votes:", voter_count)
print("------------------------------")

key_name, value = name_the_key(mydict, 'Khan')
key_name, value1 = name_the_key(mydict2, 'Khan')
message1 = 'Khan: {}%'
msgtofile1 = str(message1.format(round(value*100)))
msgtofile2 = str((value1))
print(message1.format(round(value*100)),"(",value1,")")

key_name, value = name_the_key(mydict, 'Correy')
key_name, value1 = name_the_key(mydict2, 'Correy')
message2 = 'Correy: {}%'
msgtofile3 = str(message2.format(round(value*100)))
msgtofile4 = str((value1))
print(message2.format(round(value*100)),"(",value1,")")

key_name, value = name_the_key(mydict, 'Li')
key_name, value1 = name_the_key(mydict2, 'Li')
message3 = 'Li: {}%'
msgtofile5 = str(message3.format(round(value*100)))
msgtofile6 = str((value1))
print(message3.format(round(value*100)),"(",value1,")")

key_name, value = name_the_key(mydict, "O'Tooley")
key_name, value1 = name_the_key(mydict2, "O'Tooley")
message4 = "O'Tooley: {}%"
msgtofile7 = str(message4.format(round(value*100)))
msgtofile8 = str((value1))
print(message4.format(round(value*100)),"(",value1,")")

def winner1():  
     v=list(candidate_percent.values())
     k=list(candidate_percent.keys())
     return k[v.index(max(v))]

print("------------------------------")
print("The winner is", winner1())
print("------------------------------")


# file writer

voter_countmsg = str(voter_count)

f= open("analysis2.txt","w")
f.write("Election Results\n")
f.write("----------------------------------\n")

f.write("Total Votes:" + "" + voter_countmsg + "\n")

f.write("----------------------------------\n")

f.write(msgtofile1 + "(" + msgtofile2 + ")" + "\n")
f.write(msgtofile3 + "(" + msgtofile4 + ")" + "\n")
f.write(msgtofile5 + "(" + msgtofile6 + ")" + "\n")
f.write(msgtofile7 + "(" + msgtofile8 + ")" + "\n")

f.write("----------------------------------\n")

f.write("The winner is" + " " + winner1())

f.close()