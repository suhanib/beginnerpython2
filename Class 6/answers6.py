#Try it on your own
grocerylist = ["eggs", "apples", "milk", "choclate", "instant coffee", "plastic cups", "chips"]
print(grocerylist[0])
print(grocerylist[1])
print(grocerylist[2])
print(grocerylist[3])
print(grocerylist[4])
print(grocerylist[4:6])
grocerylist[6] = "dried chili"
print(grocerylist)
grocerylist[4] = "dog food"
print(grocerylist)
grocerylist.append("ice cream")
print(grocerylist)
grocerylist.remove("apples")
print(grocerylist)
print("-------------")
# QUESTION 1: make a list and print out every item in a list one at a time. do not do print(listName).
list1 = ["apples", "grapes", "eggs", "milk"]
print(list1[0:len(list1)])
for i in range(0,len(list1)):
    print(list1[i])
print("-------------")
# QUESTION 2: write a program to sum all items in a list
list2 = [4,5,8,2,1]
count=0
for g in range(0, len(list2)):
    #print("count before add="+str(count))
    count += list2[g]
    #print("count=" + str(count) + "; g=" + str(g))

print("Sum of all the items in the list is " + str(count) + "." )

# QUESTION 3: convert a string into an actual list, where each element is one character
string = "helloiamastring"
liststring = string
for h in range(0, len(liststring)):
    print(liststring[h])

# QUESTION 4: go through this list and make a new output list that only contains words from the first list that start with "a". 
listThree = ["apple", "hello", "awesome", "ew", "bad", "nice", "ant"]
listThreeAns = []
for indx in range(len(listThree)):
    #print(str(indx))
    if listThree[indx].startswith("a"):
        listThreeAns.append(listThree[indx])
    #print(listThreeAns) 
print(listThreeAns)       
