# CLASS 4 HOMEWORK
# put your answers in answers4.py, save the file, commit it to your branch, and then push the changes
# i'll be checking and making comments on your homework, so make sure you get it done! :)

# QUESTION 1: sum up all numbers from 1 to a number of your choice
# for example, if i choose 10, then i should print out a sum of 55

num = 7
total = 0
for i in range(1,num + 1):
    total += i
print(total)

# QUESTION 2: write a program that finds all numbers which are divisible by both 5 and 7, between 1500 and 2700 (both included)
for i in range(1500, 2701):
    if (i % 5 == 0 and i % 7 == 0):
        print(i)

# QUESTION 3: what's missing in this while loop?
x = 10
while (x > 0):
    print(x)
<<<<<<< HEAD
    # insert missing code
print("liftoff!")



=======
    x -= 1
print("liftoff!")
>>>>>>> master
