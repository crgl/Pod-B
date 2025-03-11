import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from cg import *

pal = LinearSegmentedColormap.from_list(
    "pal", [cg(i/100) for i in range(100)]
)

vals = np.arange(100)

df = pd.DataFrame({'x': vals, 'y': np.sin(vals / 10), 'hue': np.cos(vals / 2)})

if __name__ == '__main__':
    sns.scatterplot(data=df, x='x', y='y', hue='hue', palette=pal)
    plt.show()
