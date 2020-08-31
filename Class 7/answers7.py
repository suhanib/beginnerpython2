EnglishToSpanish= {"mujer":"Woman", "hombre": "Man", "nina" : "girl", "nino": "boy"}
print(EnglishToSpanish)
print(EnglishToSpanish.get("nina"))
del EnglishToSpanish ["nino"]
print(EnglishToSpanish)
EnglishToSpanish["mujer"] = "woman"
print(EnglishToSpanish)

if "nina" in EnglishToSpanish:
    print("I can say this word in spanish. HORRAY!!!!:D")
else:
    print("I do not think this word is in the dictonary")

#homework
#1.




from collections import defaultdict
d = defaultdict(list)
keys = ["name", "age", "grade", "school"]
values = ["Nishka", 10, 5, "DCES"]
for keys, values in zip(keys, values):
   d[keys].append(values)

print(dict(d))

#2
favoriteColor = {"suhani":"blue", "didi":"pink", "mausam":"red", "priya":"blue", "mom":"red", "dad":"orange", "nina":"purple"}




"""
def unique(favoriteColor): 
  
    
    unique_list = [] 
      
    
    for x in range (len , favoriteColor): 
        
        if x not in unique_list: 
            unique_list.append(x) 
   
    for x in unique_list: 
        print (x) 
"""
      
#3

listTwo = [13,4,8,2,10]
 

minimum = listTwo[0]
for number in listTwo:
    if minimum > number:
       minimum = number
print (minimum)


#4

listThree = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,5,5,5,5]
def unique (listThree):
    unique_list = []
print("\nthe unique values from 3rd list is") 
print (unique(listThree))