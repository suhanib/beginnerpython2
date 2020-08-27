Dictionary = {"roloc":"purple", "dessert":"kaju katli", "age":12, "name":"Xhaiden", "number":7}
print(Dictionary.get("purple"))
print(Dictionary["number"])
print(Dictionary)
Dictionary["age"] = 13
del Dictionary["name"]
Dictionary["brothers"] = 2
print(Dictionary)
temporary = Dictionary["roloc"]
del Dictionary["roloc"]
Dictionary["color"] = temporary
print(Dictionary)
print(Dictionary.keys())
print(Dictionary.values())
if ("number" in Dictionary):
    print("numbers is a key in Dictionary")