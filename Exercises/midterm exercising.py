
## lists and loops
#%% mutability

x = 1

x = x * 3
print(x)

# %% print integers from 0 to 50

x = 0

while x < 50:
    x += 1
    print(x)

# %% pyramid function

def pyramid (n):

    x = 1

    while x <= n:
        print( "*" * x)
        x += 1
    
print(pyramid(5))
# %% lists length 

names = ["joe", "elias"]

print(len(names))

# %% accessing lists

words = ["hello", "dolly"]

print(words[0])

print(words[1])

#print(words[2]) # out of range error, lists starts from position 0 not 1

# %% function that takes a list and return each element individually


def elem_indiv (lst):
    i = 0

    while i < len(lst):
        
        print(lst[i])

        i+=1


ramones = ["Johhny", "Joey", "Dee-dee", "Tommy"]

print(elem_indiv(ramones))

print(len(ramones))

# %% element replacing

words = ["hello","my","friends"]

words[2] = "our"

print(words)

# %% element appending

words = ["hello","my","friends"]

words.append("welcome")

print(words)

# %% inserting an element

words = ["hello","my","friends"]

words.insert(2, "dear")

print(words)

# %%
words = ["hello","my","friends"]

words.pop(1)

print (words)
# %% return a string containing all elemets of a list concatenated

def to_string (lst):
    string = ""

    for item in lst:
        string = string + str(item) + " "
    return string

print(to_string(["hello", "how", "are", "you", "?"]))


# %% return list from 0 to 500

def one_to_fivehundred ():

    lst = []
    i = 0

    while i <= 500:
        lst.append(i)

        i = i + 1
    return lst

print(one_to_fivehundred())


# %% sum numbers of a list

def sum_lstnumbers (lst):

    x = 0
    i = 0

    while i < len(lst):
        x = x + lst[i]
        i = i + 1

    return x

numbers = [1,2,3,4,5,6,7,8,9]

print(sum_lstnumbers(numbers))
# %% other solutions for sum lst numbers

def sum_numbers (lst):
    x = 0

    for number in lst:
        x = x + number

    return x

numbers = [1,2,3,4,5,6,7,8,9]

print(sum_numbers(numbers))


# %% using range funtion

print(list(range(501)))

# %% find maximum in a list

def max_lst (lst):

    if len(lst) == 0:
        return None

    max = 0

    for number in lst:
        if max < number:
            max = number
    return max

lst = [12, 50, 24, 76, 30, 80, 90, 10]

print(max_lst(lst))

# %% find minimum in a lisr

def min_lst (lst):

    if len(lst) == 0:
        return None

    min = float('inf')

    for number in lst:
        if min > number:
            min = number
    return min


lst = [12, 50, 24, 76, 30, 80, 90, 10]

print(min_lst(lst))

# %% finding minimum and maximum with sorted function (other solutions)

lst = [3,2,1,4,6,1]
sorted_list = sorted(lst)

print(sorted_list[-1]) # its going to return maximum

print(sorted_list[0]) # its going to return the minimum

# %%  multiplicate without using * oprator

def multiplicate(a: int, b: int) -> int:
  """Multiplies two integers without using the * operator.

  Args:
    a: The first integer.
    b: The second integer.

  Returns:
    The product of a and b.
  """

  result = 0
  for i in range(b):
    result += a
  return result

print(multiplicate(3, 10))

# %% dictionaries ######

band = {
"johnny": "plays drums",
"joey": "plays guitar",
"markee": "sings",
"dee-dee": "plays bass-guitar"
}
for member in band:
   print(member + " " + band[member] + " in The Ramones")

# %% word frequency in dictionry

def word_frequency (text):
    wordcount = {}

    for word in text.lower().split():
        stripped_word = word.strip(".").strip(",")
        if stripped_word in wordcount:
            wordcount[stripped_word] = wordcount[stripped_word] + 1
        else:
            wordcount[stripped_word] = 1

    return wordcount



text = """
Ministerial by-elections were criticised as an inconvenience
to the government, and were argued to hold back potential
executive talent that represented marginal constituencies 
where a by-election would be risky. Nevertheless, supporters
"""

print(word_frequency(text))

## word count diagram with asterix












# %%
