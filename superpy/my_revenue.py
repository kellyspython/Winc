import pandas as pd
from my_date_time import datum, date_today


FILE_BOUGHT = "bought.csv"
FILE_SOLD = "sold.csv"


class Revenue:

    def revenue_calc(choice):     
        day = date_today()
        total_sold = 0
        if choice == "today":
            data = pd.read_csv(FILE_SOLD)
            filter = data[(data['Sell_date'] == day)]
            dataframe=pd.DataFrame(filter)
            prices = dataframe.reset_index(drop=True)
            indexes = prices.index
            for index in indexes:
                total_sold += prices.iloc[index, prices.columns.get_loc('Sell_price')] 
            print(f"Total renevue for: {day} = € {total_sold}")
        

        elif choice == "yesterday":
            # extract vaulues from File_SOLD
            data = pd.read_csv(FILE_SOLD)
            filter = data[(data['Sell_date'] == datum(1))]
            dataframe=pd.DataFrame(filter)
            prices = dataframe.reset_index(drop=True)
            indexes = prices.index
            for index in indexes:
                total_sold += prices.iloc[index, prices.columns.get_loc('Sell_price')]
            print(f"Total renevue for: {datum(1)} = € {total_sold}")
        

    def rev_date_calc(given_date):
        total_sold = 0      
        # extract vaulues from File_SOLD
        data = pd.read_csv(FILE_SOLD)
        filter = data[(data['Sell_date'] == given_date)]
        dataframe=pd.DataFrame(filter)
        prices = dataframe.reset_index(drop=True)
        indexes = prices.index
        for index in indexes:
            total_sold += prices.iloc[index, prices.columns.get_loc('Sell_price')]
                    
        print(f"Total renevue for: {given_date} = € {total_sold}")