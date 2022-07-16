import random as rand
import sys

game_over = False
num_guesses = 5


def generate_number():
    x = rand.randint(0, 100)
    return x


def number_compare(x, y):
    global game_over
    global num_guesses

    if x > y:
        print("Number is higher")
        num_guesses -= 1
    elif x < y:
        print("Number is lower")
        num_guesses -= 1
    elif x == y:
        game_ends()


def game_ends():
    global game_over
    print("You won!")
    sys.exit()


def start():
    global num_guesses
    cpu_number = generate_number()
    while num_guesses > 0 and not game_over:
        print(f"Number of guesses is {num_guesses}")
        input_user = int(input("Insert number: "))
        number_compare(cpu_number, input_user)
    print("You ran out of lives.")


start()
