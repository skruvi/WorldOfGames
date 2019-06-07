# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5

# Score.py
# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.
# Methods
# 1. add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.

#import Utils
#from Live import welcome

def add_score(name):
    f = open("score.txt", "w")
    f.write(name)
    f.close()

    f = open("score.txt", "r")
    print(f.read())