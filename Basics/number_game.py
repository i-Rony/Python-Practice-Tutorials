# Limit the number of guesses
# Catch when someone submits a non-integer value
# print "too high" or "too low" messages for bad guesses
# let people play again


import random

# generate a random number between 1 to 10
secret_number = random.randint(1, 10)


def run_game():

    guesses = []
    guess = 0

    while len(guesses) < 5:
        # safely make an int
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 to 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # compare guess the secret number
            if guess == secret_number:
                # print hit/miss
                print("You got it! my number was {}".format(secret_number))
                break
            elif guess < secret_number:
                print("My number is higher than {}".format(guess))
            elif guess > secret_number:
                print("My number is lower than {}".format(guess))

            else:
                # print hit/miss
                print("That's not it!")
        guesses.append(guess)

    else:
        print("You didn'y get it! My number was {}".format(secret_number))

    play_again = input("Do you want to play again? [Y/n]")
    if play_again.lower() != 'n':
        run_game()
    else:
        print("Bye!")


run_game()
