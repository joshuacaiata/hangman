import random
from dict import word_list

def retrieve():
    w = random.choice(word_list) # retrieve random word
    return w.upper() # return the upper case of the word

def game(word):
    guessed_word = False
    used_l = []
    word_guesses = []
    word_line = "_" * len(word)
    guesses = 0

    print("Welcome to Hangman")
    display_man(guesses)
    print(word_line)

    while guessed_word == False and guesses < 6:
        guess = input("Please guess one letter, or one word: ").upper() # taking player input
        if len(guess) == 1: # if it's just a singular letter
            if guess in used_l: # if we've used the letter
                print("You have already used this letter. Please try again")
            elif guess not in word: # if we've guessed a letter that isnt in the word
                print("The chosen letter", guess, "is not in the word. Please try again.")
                guesses += 1
                used_l.append(guess)
            else: # the letter is in the word, so it was successful
                print("Yes!", guess, "is in the word!")
                used_l.append(guess)
                word_line_list = list(word_line)
                letter_places = [i for i, letter in enumerate(word) if letter == guess]
                for i in letter_places:
                    word_line_list[i] = guess
                word_line = "".join(word_line_list)
                # now we check if we guessed the word
                if "_" not in word_line:
                    guessed_word == True
        elif len(guess) == len(word): # if its a word
            if guess in word_guesses: # if we guessed the word already
                print("You can't guess the same word twice! Try again.")
            elif guess != word: # if its not word
                print(guess, "is not the word, unfortunately.")
                guesses += 1
                word_guesses.append(guess)
            else: # if it is the word
                guessed_word = True
                word_line = word
        else:
            print("That is not a valid input, please try again.") # error message, just in case

        display_man(guesses)
        print(word_line)
    
    if guessed_word:
        print("Congrats! You guessed it!")
    else:
        print("Better luck next time! The word was:", word)




def display_man(guess):
    hangman = [
        """
            ----------------
            |              |
            |
            |
            |
            |
            |
            |
            _
        """,
        """
            ----------------
            |              |
            |              O
            |
            |
            |
            |
            |
            _
        """,
        """
            ----------------
            |              |
            |              O
            |              |
            |
            |
            |
            |
            _
        """,
        """
            ----------------
            |              |
            |              O
            |             \|
            |              
            |
            |
            |
            _
        """,
        """
            ----------------
            |              |
            |              O
            |             \|/
            |              
            |
            |
            |
            _
        """,
        """
            ----------------
            |              |
            |              O
            |             \|/
            |             /
            |
            |
            |
            _
        """,
        """
            ----------------
            |              |
            |              O
            |             \|/
            |             / \\
            |
            |
            |
            _
        """,
    ]
    print(hangman[guess])

def start():
    word = retrieve()
    game(word)
    response = input("Would you like to play again? (Y or N) ").upper()
    while response == "Y":
        word = retrieve()
        game(word)
        response = input("Would you like to play again? (Y or N )").upper()

start()