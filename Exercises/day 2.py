#%%

def lst_q():
    lst = []

    i = 0

    while i <= 500:
        lst.append(i)
        i = i + 1

    return lst

print(lst_q())
    


# %% same as above but shorter solution


print(list(range(501)))

# %%

def add_numbers(lst):
    sum = 0

    for member in lst:
        sum = sum + member
    return sum

print(add_numbers([1,2,3])) 



# %%

def max_number (lst):
   if len(lst) == 0:
      return None
   
   max = lst[0]

   for i in lst:
      if i > max:
         max = i

   return max
      
print(max_number([-234, 1, 3 , -4]))
# %%

lst = [3,1,2,3,4,5]

sorted_list = sorted(lst)

print(sorted_list[-1])

#%% dictionairies

beatles = {
   "john" : " sings and does everything",
   "ringo": "plays drums, and sings",
   "paul" : "plays the bass guitar",
   "george" : "plays the guitar"
}

#%% this is a set, notice that elements arent key value pairs


vegetables = {"lettuces" , "artichoke"}

#%%

beatles = {}

beatles ["john"] = "sings and does everything"
beatles ["ringo"] = "play drums"
beatles ["paul"] = "play the bass guitar"

#%%

dictionary = {
   1: "hello",
   "pepe" : True,
   1.2 : 4

}

print(dictionary)



#%%

beatles = {
   "john" : " sings and does everything",
   "ringo": "plays drums, and sings",
   "paul" : "plays the bass guitar",
   "george" : "plays the guitar"
}


beatles["john"] = "just sings"
beatles.pop("ringo")

print(beatles)

#%%

beatles = {
   "john" : " sings and does everything",
   "ringo": "plays drums, and sings",
   "paul" : "plays the bass guitar",
   "george" : "plays the guitar"
}

print(beatles.keys())
print(beatles.values())

#%%

beatles = {
   "john" : " sings and does everything",
   "ringo": "plays drums, and sings",
   "paul" : "plays the bass guitar",
   "george" : "plays the guitar"
}

for member in beatles:
   
   
   print (member + " " + beatles[member])



#%%
















# %%
