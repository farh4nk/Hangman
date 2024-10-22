import random
import string
from words import word_list

index = random.randint(0, len(word_list)-1)
word = word_list[index]
tries = 6

def run():
    current_turn = 0
    letters = []
    display = []
    wrong_letters = []
    used_letters = []
    for letter in word:
        letters.append(letter)
        display.append("_ ")
    print("".join(display))
    while current_turn < tries:
        guess = input("Guess a letter: ")
        if guess in letters:
            for i, letter in enumerate(letters):
                # correct guess
                if guess == letter:
                    display[i] = guess
                    used_letters.append(guess)
            print("".join(display))
            # win condition
            if display == letters:
                print(f"nice job. The word was {word.upper()}")
                return
        # invalid guess
        if guess not in string.ascii_lowercase:
            print(f"{guess} is not a valid guess")
        else:
            if guess in wrong_letters:
                print("already guessed")
            if guess not in wrong_letters and guess not in used_letters:
                wrong_letters.append(guess)
                print(f"{guess.upper()} is WRONG")
                print("Used Letters: ")
                for letter in wrong_letters:
                    print(letter)
                current_turn += 1
                print("Tries Remaining: " + str(tries-current_turn))
    # lose condition
    if current_turn == tries:
        print(f"you FAILED. The word was {word.upper()}")


run()
