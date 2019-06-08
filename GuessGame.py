import random
from Score import score_calc

def generate_number(diff):
    for x in range(10):
        secret_number = random.randint(1, int(diff))
    return secret_number

def get_guess_from_user(diff):
    user_input = input("Guess a number between 1 to %d: " % (int(diff)))
    return user_input
def compare_results(diff):

    secret = generate_number(diff)
    from_user = get_guess_from_user(diff)
    if int(secret) == int(from_user):
        print("True")
    else:
        print("False")

def play(difficult):
    diff = int(difficult)
    compare_results(diff)
    score_calc(difficult)
