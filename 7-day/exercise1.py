#Step 1 

from random import choice


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("enter a letter").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print(chosen_word)
for l in chosen_word:
    if l== guess:
        print("right")
    else:
        print("wrong")