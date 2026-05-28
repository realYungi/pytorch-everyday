# Linear Models and Example
## A simple linear model

A linear model predicts a numeric target as a weighted sum of input features plus an intercept. For a single input feature the model can be written as:

$$\text{life\_satisfaction} = \theta_0 + \theta_1 \times \text{GDP\_per\_capita}$$

Training chooses parameters $\theta_0,\theta_1$ to minimize a loss (for example mean squared error) on the training set.

*(Optional figure: the scatterplot with fitted linear regression line — include only if useful.)*

![Linear model plot](../../assets/linear_plot.png)
*Figure: Linear regression fit on the GDP vs life satisfaction dataset.*

## Example 1‑1: training and running a linear model

An example script is available in `01-linearMod.py`. The script:

- downloads and prepares the dataset of GDP per capita and life satisfaction;
- visualizes the data with a scatter plot;
- fits a model (linear regression by default, or k‑nearest neighbours when chosen);
- makes a prediction for a new GDP value (Puerto Rico in the example).

Key points from the example:

- Model selection: you can swap `LinearRegression()` for `KNeighborsRegressor(n_neighbors=3)` to compare instance‑based and model‑based approaches.
- Training: call `model.fit(X, y)` to learn parameters (or store examples, for instance methods).
- Prediction/inference: call `model.predict(X_new)` to obtain predictions for unseen inputs.

## When to prefer linear models

- Use linear models when the relationship between input and target is approximately linear, when interpretability is important, or when you need a fast, low‑resource predictor.
- If the data shows nonlinearity or more complex structure, consider richer models (polynomial features, tree ensembles, neural networks) or instance‑based methods.

## Quick reproducible example (notes)

Here is the provided example script with Python. It uses `pandas`, `scikit-learn`, and `matplotlib` to load the data, fit a model, and plot results.

```bash
python Takumi/01-linearMod.py
```