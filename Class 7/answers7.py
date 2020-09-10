myDictionary = {"name":"Anika","age": 12,"grade": 7}
print(myDictionary.get("name"))
myDictionary["school"] = "memorial"
del myDictionary["age"]
print(myDictionary)

keys = ["name", "age", "grade", "school"]
values = ["suhani", 16, 12, "hths"]

for i in range(0,len(keys)):
  personalInfo[keys[i]] = values[i]

favoriteColor = {"suhani":"blue", "didi":"pink", "mausam":"red", "priya":"blue", "mom":"red", "dad":"orange", "nina":"purple"}

for key in favoriteColor:
  if(list(favoriteColor.values()).count(favoriteColor[key])== 1):
    print(key, favoriteColor[key])

listTwo = [13,4,8,2,10]
print(min(listTwo))

smallestNum = listTwo[0]
for num in listTwo:
  if(num < smallestNum):
    smallestNum = num
print(smallestNum)