#Main for election polling problem.
import os
import csv

filepath = os.path.join('election_data.csv')


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
   
    for row in csvreader:
        #Capturing the name of each candidate into the set.
        candidates.add(row[2])
        #Goes row by row tracking the votes.
        votes.append(row[2])
        totalvotes += 1
    
    #First the total votes in the polling data
    print("Election Results \n-------------------------")
    print(f"Total Votes: {totalvotes}\n-------------------------")

    #Reads through the set of candidate names, compares each name and counts how many times it appeared in the votes.
    #Calculates each candidates % of votes using the total.
    for candidate in candidates:
       candyvote = int(votes.count(candidate))
       print(f"{candidate}: {round((candyvote/totalvotes)*100,3)}% ({candyvote})")
       
       #After each candidates individual total votes are calculated they are compared against the current votes leader, eventually finding the greatest.
       if candyvote > winnervotes:
           winnername = candidate
           winnervotes = candyvote
       
    print(f"-------------------------\nWinner: {winnername}\n-------------------------")