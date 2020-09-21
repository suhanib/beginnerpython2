# QUESTION ONE
"""
Given a list of numbers and a number k, determine if there are three entries in the list which add up to the specified number k. 
For example, given [20, 303, 3, 4, 25] and k = 49, return true because 20 + 4 + 25 = 49.
If there is no such combination of three numbers, return false.

hint: think about nested loops.
"""
inputList = [20, 303, 3, 4, 25]
k = 49
# setting up the values we will pass into the function as parameters

def questionOne(nums, k):                   # nums is the list of numbers, k is the value they have to add up to
    result = False                          # set up a boolean variable, default false; will only change this if there is a combo present
    for a in nums:                          # these three for loops go through the list
        for b in nums:                      # for each value a takes on, b takes on every value in the list; for each value b takes on, c takes on every value in the list
            for c in nums:                  # this way, you can compare 3 numbers from the list and make sure you get every combination
                if (a != b != c):           # making sure with this if statement that they are not the same number; they need to be separate entries
                    if (a+b+c == k):        # if the sum equals k
                        print(a,b,c)        # print the combination (prints all combinations, even if the numbers are the same)
                        result = True       # set the boolean variable to true
    return result                           # return the boolean after exiting all of the for loops

print(questionOne(inputList, k))            # call the function and print the result