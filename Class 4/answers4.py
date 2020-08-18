for i in range(1,8):
    print("Vansh")

chips = 10
while(chips >0):
    print("You ate one chip.")
    chips -= 1

    import pickle

while True:
  redo_string = ["r", "yes"]
  keep_string = ["k", "no"]
  yes_list = ["Yes","yes","I would"]
  no_list = ["No","Nope","no"]

  import string, random

  def generatePassword(num):
            password = ''
            for n in range(num):
              x =random.randint(0,40)
              password += string.printable[x]
            return password


  i = 1
  website = input("What website is this password for? ")
  username = input("What is your username for this website? ")
  number_of_char_in_my_password = input("How many charecters would you like your password to have? ")
  while(i==1):
              y = generatePassword(int(number_of_char_in_my_password)) 
              print ("Your password for " + website  + " is " + y + ".                                                                                                     ")
              
              redo_password = input("Would you like to redo the password or would you like to keep this password? [R/K]")
              if redo_password.lower() in redo_string:
                  i = 1
              else:
                  i = 2
                  print("Your username for " + website + " is " + username + ".")
                  print("Your password for " + website + " is " + y + ".")
                  print("Have a nice day! Hope you use our service again! ")
  
  info = [website,username,y]
  pickle.dump(info, open("Info.dat","wb"))
  
  def generatePassword(num):
            password = ''
            for n in range(num):
              x =random.randint(0,40)
              password += string.printable[x]
            return password


  i = 1
  website = input("What website is this password for? ")
  username = input("What is your username for this website? ")
  number_of_char_in_my_password = input("How many charecters would you like your password to have? ")
  while(i==1):
              y = generatePassword(int(number_of_char_in_my_password)) 
              print ("Your password for " + website  + " is " + y + ".                                                                                                     ")
              
              redo_password = input("Would you like to redo the password or would you like to keep this password? [R/K]")
              if redo_password.lower() in redo_string:
                  i = 1
              else:
                  i = 2
                  print("Your username for " + website + " is " + username + ".")
                  print("Your password for " + website + " is " + y + ".")
                  print("Have a nice day! Hope you use our service again! ")

  info = pickle.load(open("Info.dat","rb"))
  print("your previous password was" + info) 

##import socket
##hostname= website
##hostname_ip= socket.gethostbyname(hostname)
##print(hostname_ip)



