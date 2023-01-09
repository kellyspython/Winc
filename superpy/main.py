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




    
    # stdin_fileno = sys.stdin
 
    # # Keeps reading from stdin and quits only if the word 'exit' is there
    # # This loop, by default does not terminate, since stdin is open
    # for line in stdin_fileno:
    #     # Remove trailing newline characters using strip()
    #     if 'exit' == line.strip():
    #         print('Found exit. Terminating the program')
    #         exit(0)
    #     else:
    #         print('Message from sys.stdin: ---> {} <---'.format(line))

    # stdout_fileno = sys.stdout
 
    # sample_input = ['Hi', 'Hello from AskPython', 'exit']
 
    # for ip in sample_input:
    #     # Prints to stdout
    #     stdout_fileno.write(ip + '\n')

    parser = argparse.ArgumentParser(description='Shop inventory management! example Input "productname", "count","buy date", buy_price", "exparation date" ')
    parser.add_argument('product', type=str, help='Pruduct name')
    parser.add_argument('count', type=int, help='How many products have you bought')
    parser.add_argument('buy_date', type=str, help='When did you by the product "date"')
    parser.add_argument('price', type= int, help='price off the product you pay')
    parser.add_argument('exparation', type= str, help='Whats the exparation date')

    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

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
  






if __name__ == "__main__":
    main()
