#%%
import utilities

# %%
import sys
for row in sys.path:
    print(row) # prints path of the files for modules
    

print(sys.path)
# %%

import potato # does not exist
# %%

import pandas


# %%
#Modules 

import csv
import json
import pandas

#%%

import time

while True:
    time.sleep(1)
    print("hello")

## another way of importing modules

#%%
import utilities

print(utilities.add(5,3))

#%%

from utilities import add

print(add(4,5))


#%%

# strongly not advised to use wildcard imports

from utilities import *
from other import *

print(add(5, 3))

#%% module renaming (aliasing)

import pandas as pd

#pandas.dataframe() instead
pd.dataframe()



#%%

from other import hlib

hlib()

#%% packages

import pandas.io.pickle

#%%

from utilities.math import add
# same import utilities.math.add ?
print(add(4, 3))

#%%















# %%
