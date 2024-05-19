#%%

name = "pepe"
age = 654
is_professor = True


#%%

while True:             #infinite loop
    print("oh no!")
    break

#%%

i = 0

while i < 5:
    print(i)

    i = i + 1

#%%

band = ["john" ,"joey" , "dee-dee", "tommy", "andres"]

print(band[0])

print(band[len(band)-1])
print(band[-1])

#%%

band = ["john" ,"joey" , "dee-dee", "tommy", "andres"]


band.append("pepe")

print(band)

#%%


band = ["john" ,"joey" , "dee-dee", "tommy", "andres"]


band.insert(1, "andres")
print(band)

# %%

students = ["paula" , "andres"]

band = ["john" ,"joey" , "dee-dee", "tommy", "andres"]

i = 0

while i < 2:
    band.insert (1, students[i])
    i += 1

    print(band)


# %%

students = ["paula" , "andres"]

band = ["john" ,"joey" , "dee-dee", "tommy", "andres"]

i = 0

while i < 2:
    band.insert (1, students[i])
    i += 1

band.pop(2)
band.pop(1)


print(band)


# %%


def sum (a , b):
    return a + b

#%%

ramones = ["john" ,"joey" , "dee-dee", "tommy", "andres"]
for member in ramones:
    print(member)


# %%

band = ["john" ,"joey" , "dee-dee", "tommy", "andres"]

i = 0
while i < len(band):
    print(ramones[i])
    i+=1

#%%

bands = [
    ["jonny", "joey" , "deedee" , "tomy"]
    ["george" , "ringo" , "john", "paul"]

]

for band in bands:
    for member in band:
        print(member)

#%%

def to_string (band):
    result = ""

    for item in band:
        result = result + " " + item  # to have space between them

    return result

print(to_string(["hello" , "dolly"]))

















        














# %%
