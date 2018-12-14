#Import the os and module for reading CSV file
import os
import csv

total_votes = 0

#Establish CSV path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Read file using CSV module
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
   
    next(csvreader, None) 
    for row in csvreader:
        
         # Total number of votes cast in the election
        total_votes = total_votes + 1
        
        # List of Candidates
        candidate = set(row[2])
        
    print("Total Votes: " + str(total_votes))
    print(candidate) 
# =============================================================================
#         
#         if Candidate == "Khan":
#                 print("Khan" + + )
#             elif Candidate == "Correy":
#                 print("Correy" + + )
#             elif Candidate == "Li":
#                 print("Li" + + )
#             else:
#                 print("O'Tooley" + + )
# =============================================================================
           