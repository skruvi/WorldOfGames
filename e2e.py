from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time


def test_scores_service():
    driver = webdriver.Chrome(executable_path="C:\\DevOps Course\\chromedriver")
    driver.get("http://127.0.0.1:8777/")
    score_val = driver.find_element_by_id('score').text
    time.sleep(10)
    driver.close()
    print(score_val)

    if 0 <int(score_val)< 1000:
        return True
    else:
        return False



def main_function():

    test_score = test_scores_service()

    if test_score != True:
        print("your score table is out of range")
        sys.exit(1)



