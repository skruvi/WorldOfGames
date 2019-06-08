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

#from Utils import score_file_name
import Live

def score_calc(diffcult):
    POINTS_OF_WINNING = (int(diffcult) * 3) + 5
    print(POINTS_OF_WINNING)
    add_score(POINTS_OF_WINNING)


def add_score(POINTS_OF_WINNING):
    new_file = open("Scores.txt", "w")
    print(POINTS_OF_WINNING)
    new_file.write(str(POINTS_OF_WINNING))
    new_file.close()



