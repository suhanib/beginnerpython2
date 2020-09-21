# CLASS 9 HOMEWORK
# put your answers in answers9.py, save the file, commit it to your branch, and then push the changes
# i'll be checking and making comments on your homework, so make sure you get it done! :)

# QUESTION 1: create a number-guessing game! choose a number, and ask the user to guess what number you chose, continuing to ask until they get it right
num = 7
guess = 0
while (num != guess):
    guess = int(input("what number am i thinking of? "))
print("you've guessed it correctly!")

# QUESTION 2: write a function that takes a dictionary and writes the contents into a separate file;
# the file should have two columns, one for all the keys and one for all the values
"""
    sampleOutput (separate file):
    1 one
    2 two
    3 three
"""
numbers = {4:"one", 3:"two", 2:"three"}
def questionTwo(d):
    f = open("questionTwo.txt", "w")
    for key in d:
        f.write(str(key) + " " + d[key] + "\n")
    f.close()
questionTwo(numbers)

# QUESTION 3: create a text file with some questions and answers in it. 
# read the file and make the user answer the questions from the file. 
# save the user's answers and compare them to your answers. create a new output
# file which says whether they got each question right or wrong as well as their total score

f = open("questionThree.txt", "r")
questions = {}

for line in f:
    splitString = line.strip().split(",")
    questions[splitString[0]] = splitString[1]
f.close()

counter = 0
f = open("result.txt", "w")
for key in questions:
    userAnswer = input(key)
    if (userAnswer == questions[key]):
        f.write("right\n")
        counter+=1
    else:
        f.write("wrong\n")
f.write("your score: " + str(counter))
f.close()