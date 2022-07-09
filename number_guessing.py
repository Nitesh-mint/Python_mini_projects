import random
guesses = []
print("I am thinking of a number between 0 and 20.")
number = random.randint(0,4)
while True:
    u_number = int(input("Guess it please."))
    guesses.append(u_number)
    if u_number > number:
        print("Little lower")
    elif u_number < number:
        print("A litter higher than that.")
    elif u_number == number:
        print("Fuck that's true.You guessed it in\t"+str(len(guesses))+ "\ttires.")
        break