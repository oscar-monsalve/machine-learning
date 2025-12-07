from sklearn.datasets import load_iris

data = load_iris()

X, y = data["data"], data["target"]

# Print the first 10 elements in the array. These are measurements or feautures.
print("First 10 elements of the dataset:")
print(f"{X[:10]}\n")

# X.shape tells how many rows (samples) and columns (features) there are. 150 samples, and 4 features.
print("Shape or dimensions of the dataset:")
print(f"{X.shape}\n")

# For a given sample (row), there is a corresponding "label" or specie: Iris setosa, Iris virginica or Iris versicolor.
# These species are encoded with the numbers 0, 1, and 2.
print("Label or species encoded with 0, 1, and 2:")
print(f"{y}\n")
