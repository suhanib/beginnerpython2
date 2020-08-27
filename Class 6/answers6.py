groceryList = ["Carrots", "Apples", "Bananas", "Food"]

print(groceryList[1:4])

groceryList.append("Salad")
print(groceryList)
groceryList.insert(2, "Berries")
print(groceryList)

del groceryList[2]
print(groceryList)

groceryList.remove(1)