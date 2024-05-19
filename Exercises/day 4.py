
#%%  opening files

file = open("names.txt")

print(file)
print(type(file))


# %% printing lines and closing files

file = open("names.txt")

for line in file:
    print(line)

file.close()

# %% automatic close file with "with"

with open ("names.txt") as file:

    for line in file:
        print(line)


#%%

with open ("hello.txt", "w") as file:

    file.write("hello everyboody")

#%% comma separated values (CSV) exercices

with open("users.csv") as file:

  for line in file:
      cells = line.strip().split(",")
      for cell in cells:
          print(cell)

file.close()

#%% paths

# relative path

open ("users.csv")

#/users/pepgracia/potato/tomato.txt

with open ("/users/pepgracia/potato/tomato.txt") as file:
    for line in file:
        print(line)
#%%

users = [
    ["pepe" , 33]
    ["jc", 25]
]

#%%

import csv

with open ("users.csv") as file:
    reader = csv.reader(file)

    for line in reader:
        for cell in line:
            print(cell)

with open ("users.csv") as file:
    reader = csv.reader(file)
   
    for line in reader: # to print first cell in each line !!
        print(line[0])


# %% write a file

users = [
    ["pepe" , 33],
    ["jc", 25],
    ["other", 36],
    ["larbi", 24]
]

with open ("class.csv", "w") as file:
    writer = csv.writer(file)

    for user in users:
        writer.writerow(user)

#%%
    





