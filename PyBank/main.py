import os
import csv

revenue = []
date = []

with open('BankData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    next(readCSV)

    monthrow = 0
    for row in readCSV:
        date.append(row[0])
        revenue.append(row[1])
        monthrow+= 1

greatestinc = revenue[0]
greatestdec = revenue[0]
totalrev=0

for h in revenue:
    totalrev += int(h)
for i in range(len(revenue)):
    if revenue[i] >= greatestinc:
        greatestinc = revenue[i]
        greatestincmonth = date[i]
    elif revenue[i] <= greatestdec:
        greatestdec = revenue[i]
        greatestdecmonth = date[i]

averagechange = round(totalrev/monthrow, 2)

textoutput = os.path.join('..','Pybank','budget_summary.txt')
with open (textoutput, 'w', newline='') as budget:
    write = csv.writer(budget) 
    write.writerows([
        ["Financial Analysis for budget_data.csv"],
        ["============="],
        ["Total Revenue: $" + str(totalrev)],
        ["Total Months:" + str(monthrow)],
        ["Average Revenue Change:" + str(averagechange)],
        ["Greatest Increase in Profit:" + str(greatestincmonth) + "($)"+str(greatestinc)+")"],
        ["Greatest Decrease in Profit:" + str(greatestdecmonth) + "($"+str(greatestdec)+")"],
    ])

print("Financial Analysis") 
print("=============") 
print("Total Months:" + str(monthrow))
print("Total Revenue:" + str(totalrev))
print("Average Revenue Change:" + str(averagechange))
print("Greatest Increase in Profit:" + str(greatestincmonth) + "($" + str(greatestinc)+")")
print("Greatest Decrease in Profit:" + str(greatestincmonth) + "($" + str(greatestdec)+")")    
