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
    #Declares select_day which calls datetime.date() and takes three (3) integer arguments: current year (int(get_today[0])), current month (int(get_today[1]))
    select_day= datetime.date(int(today[0]), int(today[1]), int(today[2]))
    #Declares min_days which uses timedelta and passes an integer, (10)
    min_days = datetime.timedelta(days)
    #Declares dday which subtracts payday from chqday
    dday= select_day - min_days
    #printing dday
    day = dday.strftime("%d-%m-%Y")
    return day


