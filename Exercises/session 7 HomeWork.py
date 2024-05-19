
#%%
import csv
import json

def load_file ():
    stock_list = []
    with open ("all_stocks_5yr.csv") as file:
     
        reader = csv.DictReader(file)

        #next(reader) is not needed because dict reader already understands that first row is a header not data

        for row in reader:

            stock_list.append(row)
    return stock_list 

def highest_closing_price (data):

    highest_price = 0.00 # negative float = -float("inf") & ctrl D for selecting all elements to be changed
    

    for trading_day in data:
        closing_price = float(trading_day["close"])
        trading_date = trading_day["date"]

        if highest_price < closing_price:
            highest_price = closing_price
            highest_price_date = trading_date

    return highest_price, highest_price_date


def lowest_closing_price (data):

    lowest_price = float("inf")
    

    for trading_day in data:
        closing_price = float(trading_day["close"])
        trading_date = trading_day["date"]

        if lowest_price > closing_price:
            lowest_price = closing_price
            lowest_price_date = trading_date

    return lowest_price, lowest_price_date

def average_volume (data):

    total_volume = 0
    volume_count = 0
    
    

    for trading_day in data:
        volume_count = volume_count+1
        total_volume = total_volume + int(trading_day["volume"])

    average_volume = total_volume/volume_count

    return average_volume

def price_on_date (data, date):

    for trading_day in data:
        
        if date == trading_day["date"]:
            print (trading_day["open"], trading_day["high"], trading_day["low"], trading_day["close"], trading_day["volume"])
            # or return row


def save_to_json (data):


    with open ("all_stocks_5yr.json", "w") as file:

        json.dump(data, file)

# save_to_json(load_file())


keep_going = True

while keep_going:
    print("\nWelcome to the Stock Analysis Tool!")
    print("1. View Highest Closing Price")
    print("2. View Lowest Closing Price")
    print("3. Calculate Average Trading Volume")
    print("4. Get Stock Details for a Specific Date")
    print("5. Exit")
    
    
    choice = input("Please choose 1-5: ")

    
    if choice == '1':
    

        print(highest_closing_price(load_file()))

    elif choice == '2':
        

        print(lowest_closing_price(load_file()))

    elif choice == '3':


        print(average_volume (load_file()))

    elif choice == '4':

        date = input("Please enter date in the following format year-month-day(2000-02-26): ")
        
        print(price_on_date (load_file(), date))

    elif choice == '5':
        print("\nGoodbye!")

        break
    
    else:
        
        print("\nInvalid choice. Please enter a valid option (1-5).")






    







#%%

    