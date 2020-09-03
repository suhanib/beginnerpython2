#Dictionary
Aboutme = {"name": "Sara", "fav color":"pink", "fav fruit":"mango"}
del Aboutme["name"]
print(Aboutme)

# QUESTION 1: write a program that uses a loop to take a list of keys and a list of values and 
# combine them into a dictionary.
keys = ["name", "age", "grade", "school"]
values = ["suhani", 16, 12, "hths"]
dictionary = {}
for dictionaryKeys in range(len(keys)):
    dictionary["name"] = "suhani"
    dictionary[keys[dictionaryKeys]] = values[dictionaryKeys]
print(dictionary)

# QUESTION 2: write a program that prints all the keys and values of only the unique values in the dictionary.
favoriteColor = {"suhani":"blue", "didi":"pink", "mausam":"red", "priya":"blue", "mom":"red", "dad":"orange", "nina":"purple"}
# expected output: (because blue and red are repeated values)
#   didi pink
#   dad orange
#   nina purple

for keys in favoriteColor:
    list(favoriteColor.values()).count(favoriteColor[keys]) == 1):
print(key, favoriteColor[keys])

# QUESTION 3: write a program to get the smallest item in an unsorted list.
listTwo = [13,4,8,2,10]
lowest = listTwo[0]
for j in range(len(listTwo) - 1):
    if listTwo[j+1] < lowest:
        lowest = listTwo[j+1]
print(lowest)



