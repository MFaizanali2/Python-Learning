import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([1, -1, 0])
yourValue = input("Enter Your Input: ")
myDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = myDict[yourValue]

print(f"Your Choose {reverseDict[you]}\n and computer Choose {reverseDict[computer]}")

if (computer == you):
    print("Game  is Draw")
elif (computer == -1 and you == 1):
    print("You Win")
elif (computer == -1 and you == 0):
    print("You Loss")
elif (computer == 1 and you == -1):
    print("You Loss")
elif (computer == 1 and you == 0):
    print("You Win")
elif (computer == 0 and you == -1):
    print("You Win")
elif (computer == 0 and you == 1):
    print("You Loss")
else:
    print("Invalid Input")