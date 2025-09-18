import random
import os
import string
from english_words import get_english_words_set


# random_choice renvoie un mot aléatoire
def random_choice():
    web2lowerset = get_english_words_set(["web2"], lower=True)
    random_word = random.choice(list(web2lowerset))
    return random_word


# empty_spaces renvoie le mot à trouver avec des '_' si non trouvés
def empty_spaces(word_to_guess, guesses):
    returned_str = ""

    for c in word_to_guess:
        if c in guesses:
            returned_str += c + " "
        else:
            returned_str += "_ "
    return returned_str


# intro_hangman envoie l'introduction du jeu
def intro_hangman():
    print(
        "Welcome to the hangman game!🥳\n\n"
        "You'll have to guess all the letter in order to finally guess the word.\n\nIf you fail 7 time : YOU'RE DEAD\n"
    )
    input("\nPress enter whenever you're ready 🫡 ")
    clear_term()

    options = ["Random", "Choose a word"]

    user_input = ""

    input_message = "Choose your gamemode: (1 or 2)\n\n"

    for index, item in enumerate(options):
        input_message += f"{index+1}) {item}\n"

    input_message += "\nYour choice: "

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    print("\nYou picked: " + options[int(user_input) - 1])

    return user_input


# choose_gamemode permet à l'utilisateur de selectionner entre un mot aléatoire et un mot à choisir pour jouer
def choose_gamemode(user_input):
    if int(user_input) == 1 or user_input.lower() == "random":
        # RENTRE DANS LE MODE DE JEU AVEC RANDOM
        word_to_guess = random_choice()
        return word_to_guess.lower()

    if int(user_input) == 2 or user_input.lower() == "choose a word":
        # RENTRE DANS LE MODE DE JEU AVEC CHOOSE
        word_to_guess = input("Please enter the word to guess for a friend: \n")
        validation = input("Are you sure about this word ? (y/n) ")
        if validation.lower() == "y" or validation.lower() == "yes":
            os.system("clear")
        else:
            word_to_guess = input("Write a new word: ")
        return word_to_guess.lower()


# clear_term : clear le terminal (linux only)
def clear_term():

    return os.system("clear")


# ask_user demande à l'utilisateur son choix pour le tour actuel
def ask_user(guesses):
    print(f"You guessed: {guesses}\n")
    ask = True
    while ask:
        user_guess = input("Take a guess:\n").lower()

        if user_guess == " ":
            print("\nPlease answer a valid guess ! 🤬 ")
            ask = True

        elif user_guess in guesses:
            print("\nYou've already tried it, AHAH... 🥲 ")

        elif user_guess in string.punctuation:
            print("\nThere is no chance that this character is in your word ! 🧐 ")

        else:
            ask = False
            return user_guess


# check_guess vérifie la réponse de l'utilisateur et met à jour les essais restants
def check_guess(user_guess, word_to_guess, try_left):
    if user_guess == word_to_guess:
        print(f"Well played ! You guess the word '{user_guess}' ✅")
    elif user_guess in word_to_guess:
        print(f"Well played ! You guessed the letter '{user_guess}' ✅")
        input("\n\nPress enter to take a new guess ! ✍️ ")
    else:
        print(f"EEEeer !! Wrong one for '{user_guess}'")
        try_left -= 1
        input("\n\nPress enter to take a new guess ! ✍️ ")
    clear_term()
    return try_left


# check_score vérifie le score de l'utilisateur en fonction de sa derniere réponse
def check_score(user_guess, word_to_guess, score):
    # Si le guess est juste
    if user_guess in word_to_guess:
        score += word_to_guess.count(user_guess)
    # Si le guess est le mot à trouver
    if user_guess == word_to_guess:
        score = len(word_to_guess) + 1
    return score


# win renvoie un message de fin et sort de la boucle
def win(score, word_to_guess):
    started = False
    clear_term()
    print("You win ! Well played !! 🥳 ")
    print(f"You guessed the word: {word_to_guess.capitalize()}")
    print(f"\nYour final score is: {score}\n\n")
    return started


# lose renvoie un message de fin et sort de la boucle
def lose(word_to_guess):
    started = False
    clear_term()
    print("You lose 👎 ")
    print(f"The word was {word_to_guess.capitalize()} 🤭 \n\n")
    return started


def restart_game():
    options = ["Yes", "No"]

    user_input = ""

    input_message = "Do you want to restart the game ? (1 or 2)\n\n"

    # Affichage
    for index, item in enumerate(options):
        input_message += f"{index+1}) {item}\n"

    input_message += "\nYour choice: "

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    if int(user_input) == 1 or user_input.lower() == "yes":
        return hangman_game()
    else:
        print("Thanks for playing !")


# main est le point d'entré du jeu
def main(word_to_guess):
    # Debut du jeu
    started = True
    score = 0
    try_left = 7
    guesses = []

    while started:

        print(f"Try left: {try_left}")
        print(f"Your score: {score}\n")
        # Montre le mot peu à peu deviné
        print(f"\n{empty_spaces(word_to_guess, guesses)}")

        # Demande un guess
        user_guess = ask_user(guesses)

        guesses.append(user_guess)

        # Affiche la validité de la réponse
        try_left = check_guess(user_guess, word_to_guess, try_left)

        # Mise à jour des stats
        score = check_score(user_guess, word_to_guess, score)

        # Condition d'arrêt du jeu
        if score >= len(word_to_guess):
            started = win(score, word_to_guess)
        elif try_left == 0:
            started = lose(word_to_guess)
        else:
            continue

    return score


# hangman_game est le jeu complet
def hangman_game():
    clear_term()

    user_input = intro_hangman()

    word_to_guess = choose_gamemode(user_input).lower()

    clear_term()

    # Debut du jeu
    main(word_to_guess)

    restart_game()


hangman_game()
