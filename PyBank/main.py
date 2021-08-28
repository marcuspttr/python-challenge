#Main for banking accounting problem.
import os
import csv

filepath = os.path.join('/Users/marcu/Desktop/Data_Class/python/python-challenge/PyBank/Resources/budget_data.csv')


with open(filepath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    next(csvreader, None)
    
    #date will dollect all of the months into one list
    date = []
    
    #money will calculate the total changes in net profits
    money = 0
    
    #These variables will be used to determine greatest increase and decrease in net profits and track when they occurred.
    #Previous will be used to calculate the rate of change from month to month. Needs to start at 0 so it doesn't break on starting.
    #Note rate of change is determined by: Net Profit - Previous month's Net Profit
    greatest = 0
    greatdate = "TBD"
    least = 0
    leastdate = "TBD"
    previous = 0
    changes = []
    
    #The output file will be used to collect all the printed text to be put into the .txt file.
    output = []

    #As we read through each row of the banking information.
    for row in csvreader:
        
        #Capturing each month and total money as we go. Calculating the netprofit as previously discussed.
        months = row[0]
        netprofit = int(row[1])
        date.append(months)
        money += int(netprofit)
        change = netprofit - previous
        changes.append(change)
        
        #Checking if the current rate of change is the greatest seen so far, if it is keep track of the date.
        #Note: decided to do these calculations here because we have simultaneous access to the rates of change along with the corresponding months they happened in.
        if change > greatest:
            greatest = change
            greatdate = months
        #Same idea except for greatest decrease.
        elif change < least:
            least = change
            leastdate = months
        
        #Storing the current netprofit for reference of the calculations for the next row.
        previous = netprofit
    
    #We captured all of the changes into a list. The first value is not a net change, but instead the initial value (you need two values [months] for a change).
    #Thus we removed that value form the list when computinthe average.
    changes.pop(0)
    totalchange = 0
    for monthly in changes:
        totalchange += monthly

   
    #Printing all of the financial summary calculations.
    #Each is followed by output.append where we are also adding the text for the .txt output file.
    print("Financial Analysis \n----------------------------")
    output.append("Financial Analysis\n----------------------------")
    
    print(f"Total Months: {len(date)}")
    output.append(f"\nTotal Months: {len(date)}")

    print(f"Total: ${money}")
    output.append(f"\nTotal: ${money}")

    #Average change calculation, rounded to 2 decimals as it represents a dollar amount.
    print(f"Average Change: ${round(totalchange/len(changes),2)}")
    output.append(f"\nAverage Change: ${round(totalchange/len(changes),2)}")


    print(f"\nGreatest Increase in Profits: {greatdate} (${greatest})")
    output.append(f"\nGreatest Increase in Profits: {greatdate} (${greatest})")

    print(f"Greatest Decrrease in Profits: {leastdate} (${least})")
    output.append(f"\nGreatest Decrrease in Profits: {leastdate} (${least})")

#Declaring the text file we will be making
textfile = open('/Users/marcu/Desktop/Data_Class/python/python-challenge/PyBank/Resources/bank.txt','w')

#It's currently in a big list, so this will loop through it to print it out in the .txt file.
for i in range(len(output)):
    textfile.write(output[i])