# NUMBER GUESSING GAME
# computer picks a random number, user guesses with hints like "too high/too low",tracks
#number of attempts.
#-----------------------------------------------------------------------------

import random
secret_number = random.randint(1, 100)
# secret_number=56

attempts = 0

print("Welcome to Number Guessing Game! ")
print("Guess the number between 1 to 100 : ")

while True:
    guess = int(input("Enter your guess : "))
    attempts +=1

    if guess < secret_number:
        print("Too Low! Try again...")

    elif guess > secret_number:
        print("Too high!!! Try again....")
    else:
        print("Correct!! You guessed the number YAYYYYYY!!!!!!")
        print("Total attempts : " , attempts)
        break
