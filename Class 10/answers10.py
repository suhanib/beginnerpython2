# QUESTION 2
"""
A fixed point in a list is an element whose value is equal to its index.
Given a sorted list of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2.
Given [1, 5, 7, 8] you should return False.
"""
numList = [-6, 5, 2, 8]

def fixed_point_finder(numList):
    for i in range(0, len(numList)):
        if(i == numList[i]):
            return(i)
        else:
            return("False")
print(fixed_point_finder(numList))

# QUESTION 4
"""
On election day, a voting machine writes data in the form (voterId, candidateId) to a text file.
voterId and candidateId are integers.

Write a program that reads this file and returns the winner.
If you find a voter voting more than once, report this as a fraud.

use the voterData.txt file included in this folder to solve this question.
"""
r = open("voterData.txt", "r")
voters = []
votes = []
numVotes
for line in r:
    ballot = line.split(",").strip()
    if (ballot[0] not in voters):
        voters.append(ballot[0])
        votes.append(ballot[1])
    else:
        votes.remove(ballot[1])
        print("Voter number " + str(ballot[0]) + "FRAUD, You voted more than once and your vote is not valid")
numVotes.append(votes.count(1))
numVotes.append(votes.count(2))
numVotes.append(votes.count(3))
numVotes.append(votes.count(4))
numVotes.append(votes.count(5))
numVotes.append(votes.count(6))
numVotes.append(votes.count(7))
numVotes.append(votes.count(8))
numVotes.append(votes.count(9))
numVotes.append(votes.count(10))

winner = numVotes[0]
for i in range(0, len(numVotes)):
    if(numVotes[i] > winner):
        winner = numVotes[i]
print(winner)