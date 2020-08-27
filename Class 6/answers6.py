groceryList = ["bread", "peanuts", "pears","banana bread","lemonade"]
print(groceryList[4])
print(groceryList[1:4])
groceryList.append("chicken nuggets")
print(groceryList)
del groceryList[4]
print(groceryList.pop(3))
groceryList.remove("pears")
print(len(groceryList))

listOne = ["i", "am", "a", "sentence"]
for i in range (0,len(listOne)):
  print(listOne[i])

listTwo = [4,3,6,10,32,86]
total = 0
for i in range(0,len(listTwo)):
  total += listTwo [i]
print(total)

string = "helloiamastring"
stringList = []
for i in range(0,len(string)):
  stringList.append(string[i])
print(stringList)

listThree = ["apple", "hello", "awesome", "ew", "bad", "nice", "ant"]
output = []
for i in range(0, len(listThree)):
  if (listThree[i].startswith("a")):
    output.append(listThree[i])
print(output)

