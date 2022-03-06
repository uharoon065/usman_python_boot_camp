'''
there are  two players in this game
{
    player1: 
    role of player 1:
    1: pick a word ( the word to be guessed has to be represented by ---)
    each dash represents a letter of the word
pick a incorrect attempts you are  allowing the player 2 to make
    }

{
     player2 : 
     guess a letter  or word
     }

     {
     Rules to play the game:
     if the letter is correct the letter is replaced by  the dash in the word
     if the letter is not found inthe word  the player loses its one attempt
     the player  can also guess the whole word
if the word is correct the player  wins the whole game
otherwise the player 2 gets its attempt  taken
the player 2 can also wins  by guessing all the letters in the word before the incorrect attempts are over
if player2 makes  more then allowed  incorrect attempts  he will lose
     }
'''
#Step 5

import random
from replit import clear


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])