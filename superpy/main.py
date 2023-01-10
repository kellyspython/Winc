# Imports
import random
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    fields = ['id','Product Name', 'Count','Buy date', 'Buy Price', 'Expiration Date']
    filename = "bought.csv" 
    try:
        with open(filename, mode ='r')as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                pass
                #print(lines)
    
    except FileNotFoundError:

        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)

    def report():
        pass
    
    def test():
        global filename
        # create the parser for the "foo" command
        
        parser = argparse.ArgumentParser(description='example Input "productname", "count","buy date", "buy_price", "exparation date" ')
        parser.add_argument('product', type=str, help='Pruduct name')
        parser.add_argument('count', type=int, help='How many products have you bought')
        parser.add_argument('buy_date', type=str, help='When did you buy the product "date"')
        parser.add_argument('price', type= int, help='price off the product you pay')
        parser.add_argument('exparation', type= str, help='Whats the exparation date')
        args = parser.parse_args()
        
        shop_list = []
        shop_list.append(random.randint(1000, 9999))
        shop_list.append(args.product)
        shop_list.append(args.count)
        shop_list.append(args.buy_date)
        shop_list.append(args.price)
        shop_list.append(args.exparation)
    

        with open(filename, 'a+', newline='') as csvfile:
      # Create a writer object from csv module
            csvwriter = csv.writer(csvfile)
       # Add contents of list as last row in the csv file
            csvwriter.writerow(shop_list)
  
        with open(filename, mode ='r')as file:
           # reading the CSV file
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                print(lines)

        if args.verbose:
            print(f"You bought {shop_list}")
        else:
            with open(filename, mode ='r')as file:
            # reading the CSV file
                csvFile = csv.reader(file)
            # displaying the contents of the CSV file
                for lines in csvFile:
                    print(lines)   
  
    parser = argparse.ArgumentParser(description='Shop inventory management!')
    FUNCTION_MAP = {'buy' : test,
                'report' : report }

    parser.add_argument('command', choices=FUNCTION_MAP.keys())

    args = parser.parse_args()

    func = FUNCTION_MAP[args.command]
    func()





if __name__ == "__main__":
    main()
