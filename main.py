# 1 for snake
# -1 for water
# 0 for gun

import random

computer = random.choice([-1, 0, 1])
yourstr = input("Enter Your Choice:- ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverse_Dict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[yourstr]

print(f"You Chose {reverse_Dict[you]}\nComputer Chose {reverse_Dict[computer]}")

if (computer == you):
    print("This is a Draw! ")
else:
    if(computer == 1 and you == -1):
        print("You Won! ")
    elif(computer == 1 and you == 0):
        print("You Won! ")
    elif(computer == -1 and you == 1):
        print("You Lost! ")
    elif(computer == -1 and you == 0):
        print("You Lost! ")
    elif(computer == 0 and you == 1):
        print("You Lost! ")
    elif(computer == 0 and you == -1):
        print("You Won! ")
    else:
        print("Error! Try Again...")