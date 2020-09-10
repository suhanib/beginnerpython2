num = 7
guess = 0 
while (num != guess):
    guess = int(input("what number am I thinking of?"))
print("you've guessed it correctly!! YAYAYAY!")    

numbers = {1:"one", 2:"two", 3:"three"}
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

f = open("result.txt", "W")
for key in questions: 
    userAnswer = input(key)
    if (userAnswer == question[key]):
        f.write("right")
        counter+=1
    else:
        f.write("wrong\n")
f.write("your score: " + str(counter))
f.close()
