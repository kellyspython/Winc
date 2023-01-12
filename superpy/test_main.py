import argparse
import random
import pandas as pd 
import csv
from datetime import date   

file_bought = "bought.csv"
file_sold = "sold.csv" 
def main():
    
    def report_bought():
        df = pd.read_csv(file_bought)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(df)

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
        shop_list.append(args.buy_date)
        shop_list.append(args.price)
        shop_list.append(args.exparation)
        print(f"You input is: {shop_list}")

        with open(file_bought,'a+', newline='') as csvfile:
        # Create a writer object from csv module
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(shop_list) 


    def ad_sell_list():
        sell_list = []

        with open(file_sold, mode ='r')as file:
            csvFile = csv.reader(file)

            random_number = random.randint(1000, 9999)
            if random_number in file:
                random_number = random.randint(1000, 9999)
        sell_list.append(random_number)     
        sell_list.append(args.bought_id)
        sell_list.append(args.sell_date)
        sell_list.append(args.sell_price)
    
        print(f"You input is: {sell_list}")

        with open(file_sold, 'a+', newline='') as csvfile:
        # Create a writer object from csv module
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(sell_list) 


    parser = argparse.ArgumentParser(description='Shop inventory management!')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')

        # Create a report subcommand    
    parser_report = subparsers.add_parser('report_bought', help='print bought report')
    parser_report.set_defaults(func=report_bought)

    parser_report = subparsers.add_parser('report_sold', help='print sold report')
    parser_report.set_defaults(func=report_sold)

        # create the parser for the "buy" command
    parser_a = subparsers.add_parser('buy', help='buy help')
    parser_a.add_argument('product', type=str, help='Product name')
    parser_a.add_argument('count', type=int, help='How many products have you bought')
    parser_a.add_argument('buy_date', type=str, help='When did you buy the product "date"')
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
    parser_d.add_argument('bought_id', type=int, help='Bought ID number')
    parser_d.add_argument('sell_date', type=str, help='Sell date')
    parser_d.add_argument('sell_price', type=int, help='Sell price')
    parser_d.set_defaults(func=ad_sell_list)

    # create the parser for the "e" command
    parser_e = subparsers.add_parser('e', help='e help')
    parser_e.add_argument('report_sold', help='How many products have you sold')



    args = parser.parse_args()
    args.func()


    
if __name__ == "__main__":
    main()