# QUESTION 4
"""
On election day, a voting machine writes data in the form (voterId, candidateId) to a text file.
voterId and candidateId are integers.

Write a program that reads this file and returns the winner.
If you find a voter voting more than once, report this as a fraud.

use the voterData.txt file included in this folder to solve this question.
"""

f = open("voterData.txt", "r")
voters = []
candidates = {}
# explanation:
#   opening the voter data file to read
#   setting up a list to hold all of the voter ids so that we can check if one has already been used in case there was a fraud
#   setting up a dictionary where the keys are the candidates and the values are how many votes they have

def checkVoter(voterId):
    if voterId not in voters:
        voters.append(voterId)
        return True
    else:
        return False
# explanation:
#   this is a function used to check if this is a valid voter or if its a fraud
#   if the voter id passed into this function is not already in the list then it is appended to the list and the function returns True because this voter is valid
#   if the voter id passed in is already in the list it returns false and we can use this to print out that it was a fraud

def addToCandidate(candidateId):
    if candidateId in candidates:
        candidates[candidateId] += 1
    else:
        candidates[candidateId] = 1
# explanation:
#   this is a function used to add to the amount of votes a candidate has received
#   if the candidate id passed in is already in the dictionary, you add 1 to the value, which is the number of votes they received
#   if the candidate id passed in is not already there, you add it to the dictionary as a new key and give it a starting value of 1 vote

for line in f:
    data = line.split(",")
    for i in range(0, len(data)):
        data[i] = int(data[i].strip())

    if (checkVoter(data[0])):
        addToCandidate(data[1])
    else:
        print("fraud, voter", data[0])
# explanation:
#   this goes through every line in the file
#   it splits the line at the comma to separate the voter id and the candidate id; this returns a list which we store in the variable data
#   it then strips each element in the data list of its extra spaces and casts them to integers which are easier to work with for adding
#   it calls the check voter function with the first element of the data list (the voter id)
#   if that function returned true it means the voter is valid so we can then call the addToCandidate function to add the vote
#   if that function returns false you print out that it was a voter fraud

maxVotes = 0
winner = ""
for key in candidates:
    if candidates[key] > maxVotes:
        winner = str(key)
        maxVotes = candidates[key]
print("the winner is candidate", winner, "with", maxVotes, "votes")
# explanation:
#   make the maxvotes and winner variables to store the candidate with the most votes for printing it out later
#   iterate through every key in the candidates dictionary
#   if the value of that key, which is the number of votes that candidate received, is higher than the current max we have stored,
#   store that candidate id in the winner variable and reset the current max to this new higher value we found
#   go through the whole dictionary and do this for each key to make sure we get the highest one

f.close()
