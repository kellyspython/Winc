import csv
from datetime import datetime as dt
import pandas as pd
from my_date_time import datum, date_today


FILE_BOUGHT = "bought.csv"
FILE_SOLD = "sold.csv"


class Revenue:

    def revenue_calc(choice):
        
        day = date_today()
        total_bought = 0
        total_sold = 0
        total_revenue = 0
        if choice == "today":
            df = pd.read_csv(FILE_BOUGHT)
            filter_df = df[(df['Buy date'] == day)]
            id_number = filter_df["id"]
            indexes = id_number.index
            for index in indexes:
                total_bought += df.iloc[index, df.columns.get_loc('Buy price')]
            
            # extract vaulues from File_SOLD
            data = pd.read_csv(FILE_SOLD)
            filter = data[(data['Sell_date'] == day)]
            dataframe=pd.DataFrame(filter)
            prices = dataframe.reset_index(drop=True)
            indexes = prices.index
            for index in indexes:
                total_sold += prices.iloc[index, prices.columns.get_loc('Sell_price')]
                    
            total_revenue = total_sold - total_bought
            print(f"Total renevue for: {day} = € {total_revenue}")
            
            
           

        elif choice == "yesterday":
            df = pd.read_csv(FILE_BOUGHT)
            filter_df = df[(df['Buy date'] == datum(1))]
            id_number = filter_df["id"]
            indexes = id_number.index
            for index in indexes:
                total_bought += df.iloc[index, df.columns.get_loc('Buy price')]
            
            # extract vaulues from File_SOLD
            data = pd.read_csv(FILE_SOLD)
            filter = data[(data['Sell_date'] == datum(1))]
            dataframe=pd.DataFrame(filter)
            prices = dataframe.reset_index(drop=True)
            indexes = prices.index
            for index in indexes:
                total_sold += prices.iloc[index, prices.columns.get_loc('Sell_price')]
                    
            total_revenue = total_sold - total_bought
            print(f"Total renevue for: {day} = € {total_revenue}")
