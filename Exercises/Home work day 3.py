  
#%%
def word_freq (text):

    word_count = {}

    for word in text.lower().split():

        stripped_word = word.strip(",").strip(".")

        if stripped_word in word_count:
            word_count[stripped_word] += 1
        else:
            word_count[stripped_word] = 1

    return word_count


text1 = "he was playing with you and you was playing with him at the basket ball court"

print (word_freq(text1))


#%%


def freq_bar (word_counts):

    Asterix = {}

    for word1 in word_counts.keys():

        Asterix[word1] = "*" * word_counts.values()

    return Asterix

word_counts1 ={
    'he': 1,
    'was': 2, 
    'playing': 2, 
    'with': 2, 
    'you': 2, 
    'and': 1, 
    'him': 1, 
    'at': 1, 
    'the': 1, 
    'basket': 1, 
    'ball': 1, 
    'court': 1
}


print(freq_bar(word_counts1))

#%%

def freq_bar(word_counts):

  asterix_counts = {}

  for word, count in word_counts.items():
    asterix_counts[word] = "*" * count
  return asterix_counts


word_counts1 ={
    'he': 1,
    'was': 2, 
    'playing': 2, 
    'with': 2, 
    'you': 2, 
    'and': 1, 
    'him': 1, 
    'at': 1, 
    'the': 1, 
    'basket': 1, 
    'ball': 1, 
    'court': 1
}

print(freq_bar(word_counts1))

# %% solution for second exercies

def diagram (dct):

    max_length = 0 

    for key in dct:
        if len(key) > max_length:
            max_length = len(key)
    
    for key, value in dct.items():
        print(key + (max_length - len(key)) * " " + ("*") * dct)









word_counts1 ={
    'he': 1,
    'was': 2, 
    'playing': 2, 
    'with': 2, 
    'you': 2, 
    'and': 1, 
    'him': 1, 
    'at': 1, 
    'the': 1, 
    'basket': 1, 
    'ball': 1, 
    'court': 1
}