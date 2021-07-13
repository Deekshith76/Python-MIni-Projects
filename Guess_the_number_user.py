import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        #randint throws an error if low and high values are same
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high,both are same 
        feedback = input(f"Is {guess} too high(H), too low(L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yayyy, the computer guessed your number {guess}, correctly")

computer_guess(100)