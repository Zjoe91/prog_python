
#%% exercise 1 correct refer to picture for different solution
import json

with open("luke.json") as file: # or mention location of the file "/users/joe/downloads/luke.json"
    luke_data = json.load(file)

print("Name:" + " " + luke_data.get("name"))
print("Height:" + " " + luke_data.get("height"))
print("Eye color:" + " " + luke_data.get("eye_color"))
print("Mass:" + " " + luke_data.get("mass"))



#%% exercise 2

import json

data = {
"name": "Pepe",
"last_name": "Garcia"
}

with open("data.json", "w") as file:
    json.dump(data, file)

# %% exercise 2 solution

import csv
import json

def format_converter (csv_path):
    json_content=[]
    #1 read csv file

    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
    
        #2 for each row in csv file, create dictionary
        for row in reader:
            row_dict = {
                "symbol": row[0],
                "name": row[1],
                "sector": row[2]
            }
            print(row_dict)
        #3 append the dict to a list
        json_content.append(row_dict)
        #4 dump said list to json file

        with open("converted.json", "w") as json_file:
            json.dump(json_content, json_file)

format_converter("data.csv")





# %%
