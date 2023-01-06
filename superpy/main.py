# Imports
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


    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        #csvwriter.writerows(rows)
    
    with open('bought.csv', mode ='r')as file:
   
    # reading the CSV file
        csvFile = csv.reader(file)
 
    # displaying the contents of the CSV file
        for lines in csvFile:
            print(lines)
 
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

    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                 help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                 const=sum, default=max,
    #                 help='sum the integers (default: find the max)')

    # args = parser.parse_args()
    # print(args.accumulate(args.integers))  

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()





if __name__ == "__main__":
    main()
