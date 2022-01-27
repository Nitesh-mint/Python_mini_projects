import random

print("\n.............Welcome to the dice roller game created by NITESH..........")

print("\nAre you ready to roll the dice ?")

# this denotes yes and is set to y as deafult
dice_roller = input("\nType y to roll the fucking dice: ")
dice_got = []  # for storing the rolled values
while dice_roller == "y":
    dice = random.randint(1, 6)

    if dice == 1:
        print(" _____")
        print("|     |")
        print("|  0  |")
        print("|_____|")
    elif dice == 2:
        print(" _____")
        print("|    0|")
        print("|     |")
        print("|0____|")
    elif dice == 3:
        print(" _____")
        print("|    0|")
        print("|  0  |")
        print("|0____|")
    elif dice == 4:
        print(" _____")
        print("|0   0|")
        print("|     |")
        print("|0___0|")
    elif dice == 5:
        print(" _____")
        print("|0   0|")
        print("|  0  |")
        print("|0___0|")
    elif dice == 6:
        print(" ____")
        print("|0  0|")
        print("|0  0|")
        print("|0__0|")
    dice_roller = input(
        "Enter y if you want to roll again and N if you want to exit: ")
    dice_got.append(dice)  # for storing it to the dice_got list
print("thank you for playing the game.")
print("these are the numbers you got", dice_got)
