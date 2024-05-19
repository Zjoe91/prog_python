#%% word frequency

def word_frequencies(text):
    wordcount = {}

    for word in text.lower().split():
        stripped_word = word.strip(",").strip(".")
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

print(word_frequencies(text))

def diagram(dct):

    max_length = 0

    for key in dct:
        if len(key) > max_length:
            max_length = len(key)

    for key, value in dct.items():
        print(key + (max_length - len(key)) * " " + "|" + ("*") * value)


diagram(word_frequencies(text))
# %%

