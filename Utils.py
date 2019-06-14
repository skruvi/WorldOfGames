import os
from MainScores import read_score
#from one import score_server


def score_file_name():
    print("Score file is Scores.txt")
    SCORES_FILE_NAME = "Scores.txt"
    print("######################add_score")
    read_score(SCORES_FILE_NAME)
    #score_server(SCORES_FILE_NAME)

#score_file_name()
def error_code():
    BAD_RETURN_CODE = "#Err666"
    print(BAD_RETURN_CODE)

def screen_cleaner():
    os.system('cls')




