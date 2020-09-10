# CLASS 9 PRACTICE
"""
import random
favNum = int((input("What's your favorite number? \n")))
favColor = input("What is your favorite color? \n")

if (random.randint(1, 2) == 1):
    print("I like " + favColor + " too, but unlike you, I don't like the number 3 less than", favNum + 3)
else:
    print("I really don't like " + favColor + " but", favNum + 1, "is one more than my favorite number just like you!" )

# CLASS 9 HOMEWORK
"""
# QUESTION 1: create a number-guessing game! choose a number, and ask the user to guess what number you chose, continuing to ask until they get it right
import random

retry = True
secret_num = random.randint(1, 10)
print("Welcome to: Guess the Number!!!\n")
while(retry):
    if (int(input("Guess a number from 1 through 10.\n")) == secret_num):
        print("Good job! You guessed it!\n")
        retry = False
    else:
        print("try again\n")


# QUESTION 2: write a function that takes a dictionary and writes the contents into a separate file;
# the file should have two columns, one for all the keys and one for all the values
"""
    sampleOutput (separate file):
    1 one
    2 two
    3 three
"""
dictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}

a = open("homework.txt", "a")

for i in range(0, len(dictionary.keys())):
    a.write(str(list(dictionary.keys())[i]) + str("  "))
    a.write(list(dictionary.values())[i] + "\n")
a.close()
# QUESTION 3: create a text file with some questions and answers in it. 
# read the file and make the user answer the questions from the file. 
# save the user's answers and compare them to your answers. create a new output
# file which says whether they got each question right or wrong as well as their total score
r = open("homework.txt", "r")

r.seek(0)
print(r.readline())
answer1 = input()
r.seek(2)
print(r.readline())
answer2 = input()
r.seek(4)
print(r.readline())
answer3 = input()
a = open("test.txt", "a")
total_score = 0
r.seek(1)
if (answer1 == r.readline()):
    a.write("You got question 1 right.")
    total_score += 1
else:
    a.write("You got question 1 wrong.")
r.seek(3)
if(answer2 == r.readline()):
    a.write("You got question 2 right.")
    total_score += 1
else:
    a.write("You got question 2 wrong.")
r.seek(5)
if (answer3 == r.readline()):
    a.write("You got question 3 right.")
    total_score += 1
else:
    a.write("You got question 3 wrong.")
a.write("Your total score is " + str(total_score) + " out of 3.")
