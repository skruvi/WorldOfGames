from Live import welcome, load_game, level
from MainScores import read_score, score_server
from Utils import score_file_name
welcome()
game_num = load_game()
level(game_num)
score_file_name()