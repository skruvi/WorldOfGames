from Live import welcome, load_game, level
from Utils import score_file_name
from e2e import main_function
import time


user_continue = 'y'
while user_continue == 'y':


    welcome()
    game_num = load_game()
    level(game_num)
    score_file_name()
    main_function()
    user_continue = input("Do you want to continue? y/n: ")
    if user_continue != 'y':
        print("Thank you for playing World of Games")
        time.sleep(3)
        exit(1)