summerbucketlist = ["go to the beach", "have a sleepover", "go shopping", "go to the pool", "eat ice cream"]
print(summerbucketlist[4])
print(summerbucketlist[0:3])

summerbucketlist.append("hangout with friends")
summerbucketlist.append("watch movies")
print(summerbucketlist)

# Question 1 answer
listOne = ["i", "am", "a", "sentence"]
for i in range(0,len(listOne)):
     print(listOne[i])

# Question 2 answer
listTwo = [4,3,6,10,32,86]
total = 0
for i in range(0,len(listTwo)):
    total += listTwo[i]
print(total)

# Qustion 3 answer
string = "helloiamastring"
stringlist = []
for i in range(0,len(string)):
    stringlist.append(string[i])
print(stringlist)

# Question 4 answer
listThree = ["apple", "hello", "awesome", "ew", "bad", "nice", "ant"]
output = []
for i in range(0, len(listThree)):
    if (listThree[i].startswith("a")):
        output.append(listThree[i])
print(output)