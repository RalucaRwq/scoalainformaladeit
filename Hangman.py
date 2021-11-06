import random
from random_word import list_of_random_words
my_word = random.choice(list_of_random_words)

def hangman(word):
    hidden_word = []
    for item in word.lower():
        if item != word[0] and item != word[-1]:
            hidden_word.append("_")
        else:
            hidden_word.append(item)
    attempt = 4
    print("Guess the following word:", " ".join(hidden_word))
    print(f"You have {attempt} attempts left.")

    already_checked = []
    count = 0
    while count < attempt:
        user_input = input("Please enter a letter:").lower()
        if user_input == "":
            print("Please introduce a letter:")
        if user_input in hidden_word:
            print("The letter is already displayed.")
        elif user_input in already_checked:
            print(f"The following letters have already been introduced: {''.join(already_checked)} ")
        else:
            if user_input in word:
                for iterator, value in enumerate(word):
                    if user_input == value:
                        hidden_word[iterator] = user_input
                print(" ".join(hidden_word))
            else:
                count += 1
                print(f"You have {attempt - count} attempts left.")
                already_checked.append(user_input)
            if "_" not in "".join(hidden_word):
                print("YOU WON!")
                break
            elif count == attempt:
                print(f"YOU LOST! The word was {word}.")


hangman(my_word)
