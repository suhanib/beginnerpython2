def add(num,num2):
    return num + num2
       
print(add(5,5))



def vowelCount(string):
    count = 0
    for char in string:
        if (char == "a"):
            count += 1
            if (char == "e"):
                count += 1
            elif (char == "i"):
                count += 1
            elif (char == "o"):
                count += 1
            elif (char == "u"):
                count += 1
        return count
    print(vowelCount("awegitoxuq"))
