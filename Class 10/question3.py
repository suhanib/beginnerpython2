# QUESTION 3
"""
Given a list of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythagorean triplet (a,b,c) is defined by the equation a^2 + b^2 = c^2

Return all possible triplets as well as a count of how many there are.

hint: think about nested loops.
"""

nums = [42, 12, 9, 13, 48, 4, 50, 39, 8, 18, 17, 27, 3, 49, 38, 36, 45, 23, 7, 37, 21, 34, 28, 20, 6, 29, 
14, 26, 5, 10, 24, 16, 41, 11, 25, 35, 31, 40, 47, 32, 15, 1, 30, 44, 33, 46, 22, 19, 43, 2]

count = 0
for a in nums:
    for b in nums:
        for c in nums:
            if (b != a and c != a and b != c):
                if (a**2 + b**2 == c**2):
                    count += 1
                    print(a, b, c)
                elif (a**2 + c**2 == b**2):
                    count += 1
                    print(a, b, c)
                elif (b**2 + c**2 == a**2):
                    count += 1
                    print(a, b, c)
print(count)

# explanation:
#   make a count variable and set it to 0 at first; it's going to hold a count of how many triplets you found
#   then you have three nested for loops so that you can find every combination of three numbers possible
#   no numbers repeat in a pythagorean triple (for example none are like 3, 4, 4) so you need to make sure none of the numbers are the same (i'm doing this with the if on line 17)
#   then i check if some combination of the numbers squared and added equals the third one
#   i check all three combinations because with the nested for loops going through the unsorted list, there's no guarantee that c is going to be the biggest one
#   if any of those combinations work, you add one to the count and print it out
#   this does return every combination and some repeats because it counts things like 3 4 5 and 3 5 4 as different things but that's okay
