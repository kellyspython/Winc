import argparse
import pandas as pd 
import csv   

filename = "bought.csv" 

def report():
    df = pd.read_csv(filename)
    print(df.head())   

def test():
    pass
parser = argparse.ArgumentParser(description='Shop inventory management!')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')


# Create a report subcommand    
parser_report = subparsers.add_parser('report', help='print report')
parser_report.set_defaults(func=report)


    # create the parser for the "a" command
parser_a = subparsers.add_parser('buy', help='buy help')
parser_a.add_argument('product', type=str, help='Product name')
parser_a.add_argument('count', type=int, help='How many products have you bought')
parser_a.add_argument('buy_date', type=str, help='When did you buy the product "date"')
parser_a.add_argument('price', type= float, help='price off the product you pay')
parser_a.add_argument('exparation', type= str, help='Whats the exparation date')

    # create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('count', type=int, help='How many products have you bought')

 # create the parser for the "c" command
parser_c = subparsers.add_parser('c', help='c help')
parser_c.add_argument('report', help='How many products have you bought')


args = parser.parse_args()
args.func()

# shop_list = []
# shop_list.append(args.product)
# shop_list.append(args.count)
# shop_list.append(args.buy_date)
# shop_list.append(args.price)
# shop_list.append(args.exparation)
# print(shop_list)