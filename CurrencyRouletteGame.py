
import random
from forex_python.converter import CurrencyRates
from Score import score_calc

def get_money_interval():

    t = random.randint(1, 101)
    return t

def get_guess_from_user_currency(interval):

    user_value = input("Please put your guess for the currency conversion of %d$ to ILS: " % int(interval))
    return user_value

def play_me(difficult):
    c = CurrencyRates()
    convert = c.get_rate('USD', 'ILS')
    d = int(difficult)
    interval = get_money_interval()
    aaa = get_guess_from_user_currency(interval)
    conversion = float(convert)*int(interval)
    low_interval = (int(conversion) - (5 - d))
    high_interval = (int(conversion) + (5 - d))
    if high_interval >= int(aaa) and int(aaa) >= low_interval:
        print(True)
        score_calc(difficult)
    else:
        print(False)





