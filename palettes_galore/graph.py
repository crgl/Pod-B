import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from cg import *
from yc import *
from bcm import *
from cw import *
from jn import *

# # pal_funcs = [cg, bcm, jn, yc, cw, nl, kds]
# names = ['cg', 'bcm', 'jn', 'yc', 'cw', 'nl', 'kds']

# pal_funcs = [cg, bcm, jn, yc, cw, nl, kds]
# names = ['cg', 'bcm', 'jn', 'yc', 'cw', 'nl', 'kds']


pal_funcs = [cg, bcm, jn, yc, cw]
names = ['cg', 'bcm', 'jn', 'yc', 'cw']

pals = []

for pal_func in pal_funcs:
    pal = LinearSegmentedColormap.from_list(
        "pal", [pal_func(i/100) for i in range(100)]
    )
    pals.append(pal)

vals = np.arange(100)

df = pd.DataFrame({'x': vals, 'y': np.sin(vals / 10), 'hue': np.cos(vals / 2)})

if __name__ == '__main__':
    fig, axes = plt.subplots(len(pals) // 3 + 1, 3, sharex=True, sharey=True, layout='constrained')
    for i, pal in enumerate(pals):
        ax = axes[i // 3, i % 3]
        plt.sca(ax)
        sns.scatterplot(data=df, x='x', y='y', hue='hue', palette=pal, legend=None)
        # sns.scatterplot(data=df, x='x', y='y', hue='hue', palette='magma', legend=None)
        plt.xticks([])
        plt.yticks([])
        plt.ylabel('')
        plt.xlabel('')
        ax.set_title(names[i])
    plt.show()
