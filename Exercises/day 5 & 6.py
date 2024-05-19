
#%%


import csv
import json

def find_cheapest_by_day(ticker):
    lowest_price = float("inf")
    cheapest_day = None

    with open ("all_stocks_5yr.csv", "r") as file:
        reader =  csv.reader(file)
        next(reader)

        for row in reader:
            if ticker == row[-1]:
                float_price = float(row[1])
                if float_price < lowest_price:
                    lowest_price = float_price
                    cheapest_day = row[0]


    return cheapest_day

print(find_cheapest_by_day("AAPL"))

#%%
import csv
def calculate_total_price(ticker, buy_date, sell_date, dollars_amount):

    buy_price = 0
    sell_price = 0

    if buy_date > sell_date:
        print("buy date needs to happen before sell date")

    with open ("all_stocks_5yr.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if ticker == row[-1]:
                if row[0] == buy_date:
                    buy_price = float(row[1])
                elif row[0] == sell_date:
                    sell_price = float(row[1])
    
    return dollars_amount / buy_price * sell_price

print(calculate_total_price("AAPL", "2013-06-03", "2014-06-03", 1000))
            


#%% check picture on phone for extra code

import json

with open ("class.json") as file:
    data = json.load(file)

    print (data)

    for student in data:
        print(student["name"])
        
        


#%%

import json

with open("class.json") as file:
    data = json.load(file)

    for student in data:
        if "is_drinking_water" in student and  student["is_drinking_water"]:
            print(student["name"] + " is hydrated")
        else:
            print(student["name"] + " should hydrate")






