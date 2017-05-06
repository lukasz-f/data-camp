import random


def guessing_game():
    random.seed()
    tries = 0
    number_to_guess = random.randint(0, 100)
    guessed_number = None
    while number_to_guess != guessed_number or guessed_number is None:
        try:
            guessed_number = int(input("Enter number:"))
        except ValueError:
            print('Enter number!')
            continue
        tries += 1
        if guessed_number == number_to_guess:
            print('Congrats! My number was {}'.format(number_to_guess))
        elif guessed_number < number_to_guess:
            print('Too small, try again.')
        elif guessed_number > number_to_guess:
            print('Too big, try again.')
    print('You made it in {} moves'.format(tries))


guessing_game()
