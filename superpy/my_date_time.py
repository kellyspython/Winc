#importing necessary functions
import datetime
from datetime import date
from datetime import datetime as dt
import pandas as pd

now = dt.now()

def date_txt_file():
    # Getting current date and time
    today_date = now.strftime("%d-%m-%Y") + '.txt'
    
    return today_date

def date_today():
    # Getting current date and time
    today = now.strftime("%d-%m-%Y")
    return today


def datum(days):
    #storing the value of date.today in a variable today
    today = str(date.today()).split('-')
    #Declares payday which calls datetime.date() and takes three (3) integer arguments: current year (int(get_today[0])), current month (int(get_today[1]))
    payday= datetime.date(int(today[0]), int(today[1]), int(today[2]))
    #Declares chqday which uses timedelta and passes an integer, (10)
    chqday = datetime.timedelta(days)
    #Declares n_payday which subtracts payday from chqday
    n_payday= payday - chqday
    #printing the payday
    day = n_payday.strftime("%d-%m-%Y")
    return day


