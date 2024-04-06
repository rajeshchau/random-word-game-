#this is a sequence of list where we have to find whether the word which random module make words of user matches with it or not...

#let's begin the program....

word_list = ["ardvark","baboon","camel"]

import random
chosen_word = random.choice(word_list)
print(f"hey , your choosen word is :{chosen_word}")

guess = input("Guess a letter: ").lower()
blanks = []

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

for blank in range (0,len(chosen_word)):
    blanks.append("_")

for i in range(0,len(chosen_word)):
    if chosen_word[i] == guess:
        blanks[i] = str(guess)
        
print(blanks)


