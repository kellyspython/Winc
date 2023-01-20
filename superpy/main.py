# Imports
import random
import argparse
import csv
from datetime import datetime as dt
import pandas as pd
from my_date_time import datum
from my_date_time import date_txt_file
from my_date_time import date_today
import os, shutil


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

file_bought = "bought.csv"
file_sold = "sold.csv"
cwd = os.getcwd()
path = os.path.join(cwd, "txt_files")
now = dt.now()
id = 0

def txt_folder():  
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)        

def report_bought():
    df = pd.read_csv(file_bought)
    df.head(3)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    txt_folder()
    write_day_file()



def report_sold():
    df = pd.read_csv(file_sold)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)


def ad_to_list(): 
    shop_list = []
    with open(file_bought, mode ='r')as file:
           # reading the CSV file
        csvFile = csv.reader(file)
            # displaying the contents of the CSV file
        random_number = random.randint(1000, 9999)
        if random_number in file:
            random_number = random.randint(1000, 9999)
    shop_list.append(random_number)     
    shop_list.append(args.product)
    shop_list.append(args.count)
    shop_list.append(date_today())
    shop_list.append(args.price)
    shop_list.append(args.exparation)
    print(f"You input is: {shop_list}")

    with open(file_bought,'a+', newline='') as csvfile:
    # Create a writer object from csv module
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(shop_list)
    txt_folder()    
    write_day_file()
     
def check_inventory():
    df = pd.read_csv(file_bought)
    check_stock = df[df["id"] == id]
    data_top = check_stock.head() 
    for row in data_top.index:
        index_nr = row
    if df.at[index_nr,'Count'] < args.sell_count:
        print(f"Out of stock. Stock = {df.at[index_nr,'Count']}")
    
    else:
        total = df.at[index_nr,'Count'] - args.sell_count
        df.at[index_nr,'Count']= total
        if total < 1:
            print("This product is now out of stock")
            df.drop(df.loc[df['Count']==0].index, inplace=True)
            
    df.to_csv(file_bought, index=False)
        
    
    

    


def ad_sell_list():
    sell_list = []
    df = pd.read_csv(file_bought)
    if args.product not in df:
        print('This product is not in stock')
    else:
        check_stock = df[df["product"] == args.product]
        id_number = check_stock["id"]
        global id
        id = int(id_number.values)
        with open(file_sold, mode ='r')as file:
            csvFile = csv.reader(file)
            random_number = random.randint(1000, 9999)
            if random_number in file:
                random_number = random.randint(1000, 9999)
        sell_list.append(random_number)     
        sell_list.append(id)
        sell_list.append(args.product)
        sell_list.append(args.sell_count)
        sell_list.append(args.sell_date)
        sell_list.append(args.sell_price)
        #number = args.sell_count
        check_inventory()
        print(f"You input is: {sell_list}")

        with open(file_sold, 'a+', newline='') as csvfile:
        # Create a writer object from csv module
            csvwriter = csv.writer(csvfile)
        csvwriter.writerow(sell_list) 

def advance_t():
    day = now.strftime("%d-%m-%Y")
    nr = args.days
    txt_file = (datum(nr)) + ".txt"
    
    try:
        os.chdir("txt_files")
        with open(txt_file, 'r') as file:
            df = pd.read_csv(file)
            print(df)
    except FileNotFoundError:
        print("File not found")

def write_day_file():
    
    data = pd.read_csv(file_bought, usecols=[1,2,4,5])
    file = date_txt_file()
    file_path = path + "\\" + file
    content = str(data)
    with open(file_path, 'w') as f:
        f.write(content)

    
def products():
    pass

def total_products():
    pass

def price_bought():
    pass

def sold_price():
    pass

def experation():
    pass

def is_expired():
    pass

parser = argparse.ArgumentParser(description='Shop inventory management!')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

    # Create a subcommand    
parser_report = subparsers.add_parser('report_bought', help='print bought report')
parser_report.set_defaults(func=report_bought)

parser_report = subparsers.add_parser('report_sold', help='print sold report')
parser_report.set_defaults(func=report_sold)

    # create the parser for the "buy" command
parser_a = subparsers.add_parser('buy', help='buy help')
parser_a.add_argument('product', type=str, help='Product name')
parser_a.add_argument('count', type=int, help='How many products have you bought')
parser_a.add_argument('price', type= float, help='price off the product you pay')
parser_a.add_argument('exparation', type= str, help='Whats the exparation date')
parser_a.set_defaults(func=ad_to_list)


    # create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('count', type=int, help='How many products have you bought')

    # create the parser for the "c" command
parser_c = subparsers.add_parser('c', help='c help')
parser_c.add_argument('report_bought', help='How many products have you bought')

     # create the parser for the "d" command
parser_d = subparsers.add_parser('sell', help='d help')
parser_d.add_argument('product', type=str, help='Productname')
parser_d.add_argument('sell_count', type=int, help='count')
parser_d.add_argument('sell_date', type=str, help='Sell date')
parser_d.add_argument('sell_price', type=float, help='Sell price')
parser_d.set_defaults(func=ad_sell_list)

   # create the parser for the "e" command
parser_e = subparsers.add_parser('e', help='e help')
parser_e.add_argument('report_sold', help='How many products have you sold')

   # create the parser for the "f" command
parser_f = subparsers.add_parser('advance_time', help='How many days back?')
parser_f.add_argument('days', type=int, help='How many products have you sold')
parser_f.set_defaults(func=advance_t)

args = parser.parse_args()
args.func()