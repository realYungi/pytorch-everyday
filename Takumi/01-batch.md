# Batch Versus Online Learning

Machine learning systems can also be classified by whether they learn from the full dataset at once (batch learning) or incrementally from a stream of incoming data (online learning).

## Batch learning

In batch learning the system is trained using all available data. Training is typically done offline: you train a model on the full dataset, then launch it into production where it applies what it learned without updating. Batch training can take a long time and requires substantial compute and memory resources.

One important issue with batch models is performance decay over time (often called data drift or model rot): the world changes while the model remains frozen, so you need to retrain periodically on up‑to‑date data. How often to retrain depends on the task — some vision models decay slowly, whereas models for fast‑moving domains (e.g. finance) may need frequent retraining.

*(Optional figure: illustration of batch learning and retraining — include only if helpful.)*

## Online learning

In online learning the system is trained incrementally by feeding it new data instances sequentially (individually or in small groups called mini‑batches). Each learning step is cheap and fast, so the model can adapt on the fly as new data arrives.

Online learning is useful for systems that must adapt rapidly to change or for settings with limited compute or memory (for example on‑device learning). It also enables training on datasets that cannot fit in memory by loading and processing chunks (out‑of‑core learning).

The tradeoffs include: online systems can react quickly but are more sensitive to bad or adversarial updates (so monitoring and the ability to roll back or pause learning are important), while batch systems are simpler to manage but may lag behind changing distributions.

*(Optional figure: online learning flowchart — include only when needed.)*

## Instance‑based Versus Model‑based Learning

Another useful distinction is how systems generalize from examples.

### Instance‑based learning

Instance‑based methods (for example k‑nearest neighbours) essentially "memorize" training examples and make predictions by comparing a new instance to stored examples using a similarity measure. Instance‑based learning is simple and works well on small datasets, but it does not scale well: it requires storing (or indexing) the training set in production and can be slow for high‑dimensional data like images.

*(Optional figure: instance‑based learning / nearest neighbours.)*

### Model‑based learning

Model‑based learning builds a parametric model from the training data and uses that model to make predictions. Training finds parameter values that minimize a loss function on the training set; the resulting trained model is then used at prediction time. Model‑based approaches scale better to large datasets and high‑dimensional inputs because the learned model is typically much smaller than the raw dataset.

*(Optional figure: model‑based learning illustration.)*

### Example: linear model

A simple example of a model‑based approach is a linear model for predicting life satisfaction from GDP per capita:

$$\text{life\_satisfaction} = \theta_0 + \theta_1 \times \text{GDP\_per\_capita}$$

Training chooses parameters $\theta_0,\theta_1$ to best fit the training data (for example by minimizing mean squared error). Once trained, the model can make fast predictions and is easy to deploy.

*(Optional note: many books include a short Scikit‑Learn example that loads data, fits a linear model, and plots predictions — include code only if you want runnable examples.)*

