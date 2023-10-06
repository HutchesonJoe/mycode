#!/usr/bin/env python3
"""A Python Script to create a MadLib"""

from random import randint, choice

def main():
    word_types = ["adjective", "verb", "noun", "another noun"]
    
    words = {}
    print(choice(word_types))
    #for word in word_types:
        #rand_number = randint(0,3)
        #user_input = input(f"Provide me with a {word_types[rand_number]}: ")
#        words[word] = user_input
        
    #print(f"Python is a {words['adjective'][randint(0,3)]} language that lets you {words['verb']} more {words['noun']} and integrate your {words['another noun']} more effectively.")

if __name__ == "__main__":
    main()




