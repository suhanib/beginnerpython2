# CLASS 6 HOMEWORK
# put your answers in answers6.py, save the file, commit it to your branch, and then push the changes
# i'll be checking and making comments on your homework, so make sure you get it done! :)

# HINT: loops are very helpful to answer all of these questions!!

# QUESTION 1: make a list and print out every item in a list one at a time. do not do print(listName).
listOne = ["i", "am", "a", "sentence"]
for i in range(0,len(listOne)):
    print(listOne[i])

for item in listOne:
    print(item)

# QUESTION 2: write a program to sum all items in a list
listTwo = [4,3,6,10,32,86]
total = 0
for i in range(0,len(listTwo)):
    total += listTwo[i]
print(total)

count = 0
for num in listTwo:
    count += num
print(count)

# QUESTION 3: convert a string into an actual list, where each element is one character
string = "hello i am a string"
stringList = []
for i in range(0, len(string)):
    stringList.append(string[i])
print(stringList)

stringListTwo = []
for letter in string:
    stringListTwo.append(letter)
print(stringListTwo)

# QUESTION 4: go through this list and make a new output list that only contains words from the first list that start with "a". 
listThree = ["apple", "hello", "awesome", "ew", "bad", "nice", "ant"]
output = []
for i in range(0, len(listThree)):
    if (listThree[i].startswith("a")):
        output.append(listThree[i])
print(output)

outputTwo = []
for item in listThree:
    if (item.startswith("a")):
        outputTwo.append(item)
print(outputTwo)

# FOR EACH LOOP
for item in listThree:
    print(item)