import random
import string

from words import words # second 'words' is name of the list while the first 'words' is name of python file

def get_valid_word(words):
    word = random.choice(words) #randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) 
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)#letters in the word, no duplicates
    alphabet = set(string.ascii_uppercase) #will give the uppercase letters 'ABCDEF....'
    used_letters = set() # what the user has guessed
    lives = 7

    while(len(word_letters) > 0) and lives > 0:
        # letters used
        print("You have", lives,'lives left and you have already used these letters: '," ".join(used_letters))
        
        #what current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: "," ".join(word_list))
        #getting user input
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters: #if it is a valid character in alphabet that i havent used yet
            used_letters.add(user_letter) #adding it to used_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter) #removing user_letter from word_letters
            else:
                lives = lives - 1 #takes away a life if wrong
                print("Letter not in the word")  
        elif user_letter in used_letters:
            print("You already used that character. Please try again")
        else:
            print("Invalid character. Please try again")
                   
    if lives == 0:
        print("You died, sorry. The word was ", word)
    else:
        print("You guessed the word", word, '!!')
                
hangman()
    