#%%
import colorcet as cc
import random

def bcm(x):
    i=0
    list=["#"]
    while i < 6:
        list.append(random.randint(0,abs(int(str(x)[-1]))))
        i+=1
    
    return("".join(str(x) for x in list))

print(bcm(2))
# %%
