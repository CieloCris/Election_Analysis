#Challenge 3 - PyPoll
# Election Analysis
#The data we need to retrieve
#1) The total number of votes cast
#2) A complete list of candidates who received votes
#3) The percenteage of votes each candidate won
#4) The total number of votes each candidate won
#5) The winner of the election based on popular vote.
# Assign a variable for the file to load and the path.

#Import the datetime class from the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
#Print the present time
print("The time right now is ", now)

#Add dependencies
import csv
import os

file_to_load = os.path.join('Resources', 'election_results.cvs')
with open(file_to_load) as election_data:
     print(election_data)