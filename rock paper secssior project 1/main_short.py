# we can also do that program in this way

import random

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
# ''' if (computer==-1 and you==1):  -2
#     print("You win!")

#   elif(computer==-1 and you==0):  -1
#     print("You Lose!")

#   elif(computer==1 and you==-1): 2
#     print("You Lose!")

#   elif(computer==1 and you==0): 1
#     print("You Win!")

#   elif(computer==0 and you==1): -1
#     print("You Lose!")

#   elif(computer==0 and you==-1): 1
#     print("You Win!")'''

    if((computer-you)==1 or (computer-you)==-2):
        print("You lose!")
    else:
        print("You Win!")

# the above logic is on the basis of computer-you


