
#%%
class Chair:
    
    def __init__(self, color, number_of_legs):

        if int != type(number_of_legs):
         raise ValueError ("legs must be an integer")

        self.color = color
        self.number_of_legs = number_of_legs



chair1 = Chair("black", 4)
chair2 = Chair("white", 4)
chair3 = Chair("potato", True)

print(type(chair1))
print(type(chair2))

print(chair1.color)
print(chair2.color)
print(chair1.number_of_legs)
print(chair2.number_of_legs)





# %%
