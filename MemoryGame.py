import random
import time
from os import system


def generate_sequence(difficult):
    list_of_num = random.sample(range(0, 101), int(difficult))
    for x in range(7):
        bla = "the numbers are: " + str(list_of_num)
        print(bla, end='\r')
        time.sleep(0.1)
    _ = system('cls')
    return list_of_num


def get_list_from_user():
    input_numbers = input("please type the numbers that you saw separated by whitespace ")
    user_list = input_numbers.split()
    a = list(map(int, user_list))
    return a

def is_list_equal(difficalt):
    random = generate_sequence(difficalt)
    user = get_list_from_user()

    if set(user) == set(random):
        print("True")
    else:
        print("False")

def play1(difficalt):
    is_list_equal(difficalt)


