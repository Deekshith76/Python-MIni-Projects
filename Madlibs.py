'''
String Concatenation (aka how to put strings together)
Suppose we want to create a string that says "subscribe to ____" 
'''

# youtuber = "freecodecamp channel" #some string variable

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}") #f string, much recommend

import random
# adj = input("Adjective: ")

adj = ['cool', 'amazing', 'hard', 'boring', 'exccellent']
verb1 = ['sit', 'stand','jump','fly']
verb2 = ('eat', 'stand','jump','fly')
famous_person = input("Famous person: ") #for sets {} it will not work

madlib = f"Computer programming is so {random.choice(adj)}! It makes me so excited all the time because I love to {random.choice(verb1)}. Stay hydrated and {random.choice(verb2)} like you are {famous_person}! "

print(madlib)