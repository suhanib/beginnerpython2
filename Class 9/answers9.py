# CLASS 9 PRACTICE
import random
favNum = int((input("What's your favorite number? \n")))
favColor = input("What is your favorite color? \n")

if (random.randint(1, 2) == 1):
    print("I like " + favColor + " too, but unlike you, I don't like the number 3 less than", favNum + 3)
else:
    print("I really don't like " + favColor + " but", favNum + 1, "is one more than my favorite number just like you!" )

# CLASS 9 HOMEWORK