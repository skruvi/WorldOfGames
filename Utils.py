import os
from MainScores import read_score


def score_file_name():
    print("Score file is Scores.txt")
    SCORES_FILE_NAME = "Scores.txt"
    read_score(SCORES_FILE_NAME)

def error_code():
    BAD_RETURN_CODE = "#Err666"
    print(BAD_RETURN_CODE)

def screen_cleaner():
    os.system('cls')




