import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.

I am thinking of a {}-digit number with no repeated
digits.

Try to guess what it is. Here are some clues:

What I Say:     What That Means:
Pico                One digit is correct but in the wrong 
                        position.
Fermi               One digit is correct and in the right 
                        position.
Bagels              No digit is correct.

For example, if the secret number was 248 and you 
guessed 843, the clues would be Fermi Pico'''.format(NUM_DIGITS))

    while True:  # Main game loop
        # This stores the secret number the player needs
        # to guess:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print("You have {} guesses to guess it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}:".format(num_guesses))
                guess = input(">")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They've guessed correctly, so
                # break out of the loop
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secret_num))

        # Ask the player if they want to play again.
        print("Do you want to play again (yes or no)?: ")
        if not input(">").lower().startswith("y"):
            break
        print("Thank you for playing.")


def get_secret_num():
    """Returns a string made up of NUM_DIGITS
    unique random digits."""
    numbers = list('123456789')  # Creates a list of
    # digits from 0 to 9
    random.shuffle(numbers)  # Shuffles them into
    # random order

    # Get the first NUM_DIGITS digits in the list for
    # the secret number
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with pico, fermi, bagels clues
    for a guess and secret number pair."""
    if guess == secret_num:
        return "You have chosen wisely!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their
        # original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ''.join(clues)


# If the program is run (instead of imported), run the game.
if __name__ == '__main__':
    main()
