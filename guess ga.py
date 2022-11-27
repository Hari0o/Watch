 # Guess My Number Mod 5 tries or bust


import random  

print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in five tries or less")

my_number = random.randint(1, 100)
guess = int(input("Go on, Take a guess, I dare ya "))
tries = 1

while guess != my_number:
    if guess > my_number:
        print("Lower...")
    else:
        print("Higher...")
guess = int(input("Go on, Take a guess, I dare ya "))
tries += 1
if tries==5:
        input("You failed to guess the number was it that hard?\n Press any key to exit!)"

print("Well done you guessed correctly!The number was", my_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")