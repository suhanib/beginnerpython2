# CLASS 8 HOMEWORK
# put your answers in answers8.py, save the file, commit it to your branch, and then push the changes
# i'll be checking and making comments on your homework, so make sure you get it done! :)

# QUESTION 1: write a function that takes in a list of numbers and returns the sum of all the numbers in the list.
def addList(listParam):
    total = 0
    for num in listParam:
        total += num
    return total

print(addList([1,2,3,4,5]))

# QUESTION 2: write a function that takes in a list of keys and a list of values and returns a dictionary made from those lists.
def createDictionary(keys, values):
    d = {}
    for i in range(0, len(keys)):
        d[keys[i]] = values[i]
    return d

print(createDictionary(["name", "age", "grade"], ["suhani", 16, 12]))

# QUESTION 3: write a function that takes in a string and returns how many vowels the string has.
def vowelCount(string):
    count = 0
    for char in string:
        if (char == "a"):
            count += 1
        elif (char == "e"):
            count += 1
        elif (char == "i"):
            count += 1
        elif (char == "o"):
            count += 1
        elif (char == "u"):
            count +=1
    return count
print(vowelCount("awegitoxuq"))

def vowelCountTwo(string):
    return (string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u"))
print(vowelCountTwo("awegitoxuq"))

# QUESTION 4: write a function to reverse a string.
def reverse(string):
    index = len(string) - 1
    result = ""
    while(index >= 0):
        result += string[index]
        index -= 1
    return result
print(reverse("suhani"))

def reverseTwo(string):
    result = ""
    for i in range(len(string)-1, -1, -1):
        result += string[i]
    return result
print(reverseTwo("inahus"))