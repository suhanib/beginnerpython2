# Question 1 answer
keys = ["name", "age", "grade", "school"]
values = ["suhani", 16, 12, "hths"]
personalInfo = {"name":"suhani", "age":16, "grade": 12, "school": "hths"}
for i in range(0, len(keys)):
    personalInfo[keys[1]] = values[1]
print(personalInfo)

# Question 2 answer
favoriteColor = {"suhani":"blue", "didi":"pink", "mausam":"red", "priya":"blue", "mom":"red", "dad":"orange", "nina":"purple"}
for key in favoriteColor:
   if (list(favoriteColor.values()).count(favoriteColor[key]) == 1):
       print(key, favoriteColor[key])

# Question 3 answer
listTwo = [13,4,8,2,10]
print(min(listTwo))

smallestNum = listTwo[0]
for num in listTwo:
    if (num < smallestNum):
        smallestNum = num
print(smallestNum)
# Question 4 answer
listThree = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,5,5,5,5]
output = []
for num in listThree:
    if (num not in output):
        output.append(num)
print(output)        