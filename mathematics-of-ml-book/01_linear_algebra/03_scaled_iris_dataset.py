from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# Had to add the following in order to execute the script locally (not using Jupyter notebooks)
import matplotlib
matplotlib.use("TkAgg")

data = load_iris()
X, y = data["data"], data["target"]

sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Scaling the data
X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)

# Create data
x = X_scaled.ravel()  # np.ravel() is used to convert a multi-dimensional array into a one-dimensional (flattened) array.

labels = ["sepal length", "sepal width", "petal length", "petal width"]
g = np.tile(labels, X_scaled.shape[0])
df = pd.DataFrame(dict(x=x, g=g))

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
grid = sns.FacetGrid(df, row="g", hue="g", aspect=10, height=1.5, palette=pal)

# Draw the densities
grid.map(sns.kdeplot, "x", bw_adjust=.5, clip_on=False, fill=True, alpha=1, linewidth=1.5)
grid.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)

# Add reference line
grid.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)

# Add labels to each plot
grid.map(
    lambda x, color, label:
    plt.gca().text(0, .2, label, fontweight="bold", color=color, ha="left", va="center", transform=plt.gca().transAxes),
    "x"
)

# Adjust subplots and aesthetics
grid.figure.subplots_adjust(hspace=-.25)
grid.set_titles("")
grid.set(yticks=[], ylabel="")
grid.despine(bottom=True, left=True)

plt.show()
