import random
import os
from english_words import get_english_words_set


# Random_choice renvoie un mot aléatoire
def random_choice():
    web2lowerset = get_english_words_set(["web2"], lower=True)
    random_word = random.choice(list(web2lowerset))
    return random_word


def empty_spaces(usr_str, guesses):
    returned_str = ""
    for c in usr_str:
        if c in guesses:
            returned_str += c + " "
        else:
            returned_str += "_ "
    return returned_str


def intro_hangman():
    print(
        "Welcome to the hangman game!🥳\n"
        "You'll have to guess all the letter in order to finally guess the word.\nIf you fail 10 time => YOU'RE DEAD\n"
    )
    input("Press enter whenever you're ready 🫡 ")

    options = ["Random", "Choose a word"]

    user_input = ""

    input_message = "\nPick an option:\n"

    for index, item in enumerate(options):
        input_message += f"{index+1}) {item}\n"

    input_message += "Your choice: "

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    print("\nYou picked: " + options[int(user_input) - 1])

    return user_input


def choose_gamemode(user_input):
    if int(user_input) == 1 or user_input.lower() == "random":
        # RENTRE DANS LE MODE DE JEU AVEC RANDOM
        word_to_guess = random_choice()
        return word_to_guess

    if int(user_input) == 2 or user_input.lower() == "choose a word":
        # RENTRE DANS LE MODE DE JEU AVEC CHOOSE
        word_to_guess = input("Please enter the word to guess for a friend: \n")
        validation = input(f"Are you sure about this word: {word_to_guess} (y/n): ")
        if validation.lower() == "y" or validation.lower() == "yes":
            os.system("clear")
        else:
            word_to_guess = input("Write a new word: ")
        return word_to_guess


def clear_term():
    return os.system("clear")


def hangman_game():
    started = True

    user_input = intro_hangman()

    word_to_guess = choose_gamemode(user_input)

    clear_term()
    # Debut du jeu
    started = True
    round = 1
    guesses = []
    good_answ = 0
    wrong_answ = 0
    while started:
        print(f"Round: {round}")

        if len(guesses) != 0:
            print(f"You guessed: {guesses}")
        print(f"\n{empty_spaces(word_to_guess, guesses)}")
        user_guess = input("\nTake a guess:\n").lower()
        guesses += user_guess

        # Compte les bonnes réponses
        if user_guess in word_to_guess:
            count = word_to_guess.count(user_guess)
            print(f"Well played ! You guessed the letter '{user_guess}'")
            good_answ += count
        else:
            print(f"EEEeer !! Wrong one for '{user_guess}'")
            wrong_answer += 1

        round += 1

        # Retourn au début de la boucle
        input("Press enter to take a new guess ! ✍️ ")
        clear_term()
        guesses_count = len(guesses)

        # Condition d'arrêt du jeu
        if good_answ == len(word_to_guess):
            started = False
            print("You win ! Well played !! 🥳 ")
            print(f"You guessed the word: {word_to_guess}")
        if wrong_answ >= 10:
            started = False
            print("You loose")


hangman_game()
# Pseudo-code :
# START
#   Show user an intro to the game
#   Show the rules
#   Prompt user to launch a game
#   Tell the user his number of try before die
#   For try in game:
#       Show try left
#       Prompt User for a letter
#           if letter in game:
#               Reveal letter in word
#               Break
#
#           else:
#               try -= 1
#               Break
#       if try == 0:
#           Show user "YOU LOOSE"
#       elif len(word_to_guess) == len(user_word)
#           Show user "YOU WIN"
# END
