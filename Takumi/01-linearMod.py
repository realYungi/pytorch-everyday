import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# download and prepare the data
df = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = df[["GDP per capita (USD)"]].values
y = df["Life satisfaction"].values

# visualize the data
df.plot(
    kind="scatter", 
    grid=True, 
    x="GDP per capita (USD)", 
    y="Life satisfaction")
plt.axis([23_500,62_500,4,9])
plt.show()

# select a linear model 
# model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)

# train the model
model.fit(X, y)

# make a prediction for Puerto Rico
X_new = [[33_442.8]]
print(model.predict(X_new))