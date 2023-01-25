

# SHOP INVENTORY MANAGER!

With this command line inventory manager you can manage your products. 
The products you are buying and selling. All the input is stored in two different csv files: bought.csv and sold.csv. 
When you choose report_bought it will automatically make a txt file in the folder txt_files from the inventory of that day.  

The techical elements that i used is pandas.
With Pandas i can manipulate my csv files in a more efficiant way.
pandas helps to explore, clean, and process my data.

I have tryed to use modules for my code. To get the value in the module was a bit difficult.
Also i used OS to save my files on the computer in a way that it is usefull with different OS.


You can use the following commands in this inventory manager.

Commands and Definition
buy -  Buy products for stock. You need to ad the following input after the command ‘buy’
‘product’ ‘count’ ‘price’ ‘expiration’

product = Product name
count = How many products did you buy
price =  Price per product you paid
expiration = Date that the product expired “dd-mm-yyyy”

Example command: ‘buy’ ‘apple' ‘2’ ‘24-01-2023’ ‘1.0’

sell - If you want to sell a product, use the sell command.
You need to ad the following input after the command ‘sell’
‘product’ ‘count’ ‘sell_date’ ‘sell_price’ 

product = Product name
count = How many products did you sell
sell_date = today's date
sell_price = Price per product you sold it for.

Example command: ‘sell’ ‘apple’ ‘2’ ‘24-01-2023’ ‘1.3’

products - Products in stock

revenue - Prints out the revenue from today or yesterday.
subcommands are: ‘today’ and ‘yesterday’

You can also print out the revenue with a specific date.
You can do this with the revenue_date command

revenue_date - prints out the revenue for the date you put in.
Example command: revenue_date 24-01-2023

profit - Prints out the profit from today or yesterday.
subcommands are: ‘today’ and ‘yesterday’
Example command: ‘profit’ ‘yesterday’

You can also print out the revenue with a specific date.
Do this with the profit_date command


profit_date - prints out the profit for the date you put in.
Example command: profit_date 24-01-2023

advance_time - shows the product inventory a few days back.
You can put in the number of days you want to go back in time to see the inventory on that day.
Example command: advance_time 2 
( shows the inventory from 2 days ago)

is_expired - prints all the products that are expired

report_bought - Prints out the products you bought.

report_sold - Prints out the products you sold.

	




