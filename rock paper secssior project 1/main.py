'''We all have played rock , paper , Scissors game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user.'''

import random

'''1 for Rock
-1 for Paper
0 for Scissors'''

computer= random.choice([-1,0,1])
# use random module to choice any number bet -1 0 1
youstr = input("Enter your choice:")
youDict = {"r": 1, "p": -1, "s":0 } 
# dictonary
reverseDict = {1: "Rock", -1:"Paper", 0 : "Scissors"}

you = youDict[youstr]
# by now we have 2 number(variables) , you and computer
print(f"You Choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw!")

else:

  if (computer==-1 and you==1):
    print("You win!")

  elif(computer==-1 and you==0):
    print("You Lose!")

  elif(computer==1 and you==-1):
    print("You Lose!")

  elif(computer==1 and you==0):
    print("You Win!")

  elif(computer==0 and you==1):
    print("You Lose!")

  elif(computer==0 and you==-1):
    print("You Win!")

  else:
    print("Something went wrong!")



