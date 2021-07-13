import random

def guess(x):
    random_number = random.randint(1, x) # a rand number in between 1 and x both inclusive
    guess = 0 # an impossible case 
    
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly")

guess(10)