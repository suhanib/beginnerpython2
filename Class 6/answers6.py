fruitList = ["oranges", "apples", "rasberries", "cantoloupes", "blackberries", "watermelons", "bananas", "grape", "grapefruit",
"mango", "pear", "lychee"]
print(fruitList[3])
print(fruitList[0:3])
fruitList[3] = "dragon fruit"
fruitList.append("rambutan")
print(fruitList)
fruitList.insert(2, "blueberries")
print(fruitList)
del fruitList[5:7]
print(fruitList)
fruitList.remove("apples")
print(fruitList.pop(0))
print(fruitList)