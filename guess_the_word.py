import random
import json
from difflib import *

data = json.load(open("data.json"))


list1 = []

for every_key in data.keys():
    list1.append(every_key)


with open('words.txt') as f:
    content = f.read()
    content = content.lower()


randomWords = []

for every_word in content.split('\n'):
    if every_word in list1:
        randomWords.append(every_word)
    else:
        pass

monil = random.choice(randomWords)

# print(monil)

guess_count = 5

print("*****************GUESS THE WORD*****************")

print(
    f"HINT 1: The word has {len(monil)} letters and it startswith '{monil[0].capitalize()}'\n")


while guess_count > 0:
    try:
        print(f"You have {guess_count} guesses left.\n")
        input_word = input("Guess the word: ")
        input_word = input_word.lower()
        print()
        if input_word == monil:
            print('Congrats, You guessed it right.\n')
            break
        elif guess_count == 4:
            if SequenceMatcher(None, input_word, monil).ratio() > 0.7:
                print("Wrong guess, Please try again.")
                print(f"The correct word is very similar with your input!\n")
            else:
                print("Wrong guess, Please try again.\n")
                if len(data[monil]) > 1:
                    print(
                        f"HINT 2: The meaning of the word: {''.join((data[monil])[1])}\n")
                else:
                    print(
                        f"HINT 2: The meaning of the word: {''.join(data[monil])}\n")
        elif guess_count == 1:
            print(
                f"Sorry, no guesses left! The correct word is {monil.capitalize()}.")
        else:
            if SequenceMatcher(None, input_word, monil).ratio() > 0.7:
                print("Wrong guess, Please try again.")
                print(f"The correct word is very similar with your input!\n")
            else:
                print("Wrong guess, Please try again.\n")
        guess_count -= 1
    except:
        print("Invalid Input!")
