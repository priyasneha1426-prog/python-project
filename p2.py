
import random

number = random.randint(1, 100)

print("NUMBER GUESSING GAME")

guess = random.randint(1, 100)

for i in range(1, 101):

    print("Computer's guess:", guess)

    print("Enter 0 if correct")
    print("Enter -1 if your guess should be lower")
    print("Enter 1 if your guess should be higher")

    num = int(input("Enter your choice: "))

    if num == 0:
        print("Computer guessed the correct number!")
        break

    elif num == -1:
        guess = random.randint(1, guess - 1)

    elif num == 1:
        guess = random.randint(guess + 1, 100)

    else:
        print("Invalid choice!")

else:
    print("Maximum attempts reached!")

