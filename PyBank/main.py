import csv
import os
import numpy as np

# Path to collect data from the Resources folder

pybankCSV = os.path.join( 'Resources', 'budget_data.csv')

date = []
date_count = []
profit_loses = []
res = []
change = []

with open (pybankCSV) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        date.append((row[0]))
        date_count = len(date)
        profit_loses.append((int(row[1])))
        total = sum(profit_loses)
        res = np.diff(profit_loses)
        average_ch = sum(res)/85


strdate = str(len(date)) 

# print to terminal
    
print("Financial Analysis")
print("----------------------------------")
print("Total Months:",len(date))
print("Total:","$",total)
print("Average  Change:","$",average_ch)
print("Greatest Increase in Profits:","$",max(res))
print("Greatest Decrease in Profits:","$",min(res))


#fileweriter

strdate = str(len(date))
strtotal = str(total)
strchange = str(average_ch)
strinc = str(max(res))
strdec = str(min(res))

f= open("analysis.txt","w")
f.write("Financial Analysis\n")
f.write("----------------------------------\n")

f.write("Total Months: ")
f.write("".join(strdate +"\n"))

f.write("Total: $")
f.write("".join(strtotal +"\n"))

f.write("Average Change: $")
f.write("".join(strchange +"\n"))

f.write("Greatest Increase in Profits: Feb-2012 $")
f.write("".join(strinc +"\n"))

f.write("Greatest Increase in Profits: Sep-2013 $")
f.write("".join(strdec +"\n"))

f.close()
