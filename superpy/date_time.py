#importing necessary functions
import datetime
from datetime import date
import pandas as pd

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

