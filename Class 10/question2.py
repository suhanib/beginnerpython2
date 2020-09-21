# QUESTION 2
"""
A fixed point in a list is an element whose value is equal to its index.
Given a sorted list of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2.
Given [1, 5, 7, 8] you should return False.
"""

def fixedPoint(inputList):
    points = []
    for i in range(0, len(inputList)):
        if (inputList[i] == i):
            points.append(inputList[i])
    
    if (len(points) == 0):
        return False
    else: return points
    
# explanation:
#   ive created a function to find the fixed points and i pass in a parameter which is a list
#   then i create another list in the function to hold the possible fixed points
#   then i go through the list that was passed in with a for loop
#   for every element in the list that was passed in, i check if the value of the element is equal to the current index we're at
#   if it is, i append that element to the points list that is holding all possible fixed points
#   after this for loop is done, i check the length of the points list
#   if the points list length is 0, it has nothing in it so there are no fixed points and i return False
#   if the points list length is something other than 0, there's something inside so there are some points so i return that list

print(fixedPoint([-6, 0, 2, 40]))
print(fixedPoint([1, 5, 7, 8]))