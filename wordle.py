import random
import sys
from termcolor import colored
import nltk
nltk.download('words')
from nltk.corpus import words

def print_menu():
    print("\nLet's play!")
    print("Have a guess! Type a 5 letter word!\n")

def read_random_word():
    with open("wordle/words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)

nltk.data.path.append('/work/words')
word_list = words.words()
five_letter_words = [word for word in word_list if len(word) == 5]


print_menu()
play_again = ""

while play_again != "q":
    
    word = random.choice(five_letter_words).upper()

    for attempt in range(1, 7):
        guess = input().upper()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end = "")
            elif guess [i] in word:
                print(colored(guess[i], 'yellow'), end = "")
            else:
                print(colored(guess[i], 'red'), end = "")
        print()

        if guess == word:
            print(colored(f'\nCongrats! You got the wordle in {attempt} attempts', 'green'))
            break
        elif attempt == 6:
            print(colored(f'Sorry, the wordle was {word}', 'red'))

    play_again = input("Wanna play again?\nYES: ENTER \nNO: Q")