
from MemoryGame import *
from GuessGame import *
from CurrencyRouletteGame import *


def welcome():
    name = input(str("please enter name: "))
    print("Hello " + name +" and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    print("\nPlease choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n" +
          "2. Guess Game - guess a number and see if you chose like the computer\n" +
          "3. Currency Roulette - Guess the current Currency conversion value")

    selection = input("\nplease select game number: ")
    while True:
        if int(selection) == 1:
            print("you choose a Memory Game")
            break
        elif int(selection) == 2:
            print("you choose a Guess game")
            break
        elif int(selection) == 3:
            print("you choose a Currency Roulette")
            break
        elif int(selection) not in range(0, 4):
            print("\n#############################################")
            print("your selection is not valid, Please try again")
            print("#############################################\n")
            return load_game()
    return int(selection)

def level(game):
    difficult = input("\nPlease select difficult level between 1 to 5: ")
    if game == 1:
        play1(difficult)
    elif game == 2:
        play(difficult)
    elif game == 3:
        play_me(difficult)


#if __name__ == '__main__':

#welcome()
#game_num = load_game()
#level(game_num)




