#Main for election polling problem.
import os
import csv

filepath = os.path.join('/Users/marcu/Desktop/Data_Class/python/python-challenge/PyPoll/Resources/election_data.csv')

with open(filepath,'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    next(csvreader, None) 

    #Initialize ticker that will capture the number of votes. 
    #This is not needed as I can just take the length of my vote list.
    totalvotes = 0
    
    #Candidate names are placed into a set because it does not allow duplicates.
    candidates = set()
    #Candidate names are placed into a list because it will allow for counting of duplicates.
    votes = []
    
    #Initilizing the tracker for the winner of the election. Currently filled with placeholders.
    winnername = "TBD"
    winnervotes = 0

    #Saving all of the ouput into a list to be exported later.
    output = []
    
    for row in csvreader:
        #Capturing the name of each candidate into the set.
        candidates.add(row[2])
        #Goes row by row tracking the votes.
        votes.append(row[2])
        totalvotes += 1
    
    #First the total votes in the polling data
    #Each output.append is adding the printed text to a list so it will be output later to the .txt file.
    print("Election Results \n-------------------------")
    print(f"Total Votes: {totalvotes}\n-------------------------")
    output.append(f"Election Results\n-------------------------\nTotal Votes: {totalvotes}\n-------------------------")

    #Reads through the set of candidate names, compares each name and counts how many times it appeared in the votes.
    #Calculates each candidates % of votes using the total.
    for candidate in candidates:
       candyvote = int(votes.count(candidate))
       
       print(f"{candidate}: {round((candyvote/totalvotes)*100,3)}% ({candyvote})")
       output.append(f"\n{candidate}: {round((candyvote/totalvotes)*100,3)}% ({candyvote})")

       #After each candidates individual total votes are calculated they are compared against the current votes leader, eventually finding the greatest.
       if candyvote > winnervotes:
           winnername = candidate
           winnervotes = candyvote
       
    print(f"-------------------------\nWinner: {winnername}\n-------------------------")
    output.append(f"\n-------------------------\nWinner: {winnername}\n-------------------------")

#Declaring the text file we will be making
textfile = open("/Users/marcu/Desktop/Data_Class/python/python-challenge/PyPoll/Resources/election.txt",'w')

#It's currently in a big list, so this will loop through it to print it out in the .txt file.
for i in range(len(output)):
    textfile.write(output[i])