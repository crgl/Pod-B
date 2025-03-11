#%%
import colorcet as cc
import random

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def bcm(x):
    i=0
    list=["#"]
    while i < 6:
        if random.randint(0,x) < (x/8)*2:
            list.append(alpha_lower[random.randint(0,25)])
        elif random.randint(0,x) > ((x/8)*6):
            list.append(alpha_upper[random.randint(0,25)])
        else:
            list.append(random.randint(0,abs(int(str(x)[-1]))))
        i+=1
    
    return("".join(str(x) for x in list))

# %%
