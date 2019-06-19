

#from Utils import score_file_name
import Live

def score_calc(diffcult):
    POINTS_OF_WINNING = (int(diffcult) * 3) + 5
    #print(POINTS_OF_WINNING)
    add_score(POINTS_OF_WINNING)


def add_score(POINTS_OF_WINNING):

    new_file = open("Scores.txt", "a+")
    new_file.close()

    get_score = open("Scores.txt", "r")
    current_value = get_score.read()
    get_score.close()

    if current_value == '':
        new_score = open("Scores.txt", "r+")
        new_score.write(str(POINTS_OF_WINNING))
        new_score.close()
    else:
        odd_score = int(POINTS_OF_WINNING)+int(current_value)
        new_score =open("Scores.txt", "r+")
        new_score.write(str(odd_score))
        new_score.close()

