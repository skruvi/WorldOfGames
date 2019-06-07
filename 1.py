# import random
#
# def generate_number(difficult):
#     for x in range(10):
#         secret_number = random.randint(1, int(difficult))
#     print(secret_number)
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     return secret_number
#
# def get_guess_from_user(difficult):
#     print(difficult)
#     user_input = input("Guess a number between 1 to %d: " % (int(difficult)))
#     print(user_input)
#     return user_input
# def compare_results(difficult):
#
#     secret = generate_number(difficult)
#     print(secret)
#     from_user = get_guess_from_user(difficult)
#     if secret == from_user:
#         print("True")
#     else:
#         print("False")
#
# def play(difficult):
#     compare_results(difficult)
