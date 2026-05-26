# Main Challenges of Machine Learning

<h3>Insufficient Quantity of Training Data</h3>

- Machines still need a lot of data to solve simple problems unlike humans.
- The quality of data matters more than algorithms when training a machine.


<h3>Nonrepresentative Training Data</h3>

- In order to generalize well, it is crucial that your training data be representative of the new cases you want to generalize to. The accuracy and the outcome really depends on this.

- If the sample is too small, you will have **sampling noise** (nonrepresentative data as a result of chance), but even very large samplescan be nonrepresentative if the sampling method is flawed. This is called **sampling bias**.


<h3>Poor-Quality Data & Irrelevant Features</h3>

- Obviously, if the data is noisy, has outliers, full of errors, the machine would have a hard time finding the pattern of the data.

- It is worth cleaning the data before we feed it. Get rid of outliers, and figure out if we are going to get rid of data that is missing some features.

- Make sure to get rid of irrelevant features. This process is called **Feature Engineering**


<h3>Feature Engineering</h3>

1) **Feature Selection** : Selecting the most useful features to train on among existing features
2) **Feature Extraction** : Combining existing features to produce a more useful one (as we saw earlier, dimensionality reduction algorithms can help).
3) **Creating new features** by gathering new data


<h3>Overfitting the Training Data</h3>

- Don't let your machine to overgeneralize things such as "a taxi driver ripped us off". That doesn't mean all taxi drivers are thieves.

- In ML, this is called **Overfitting**. This means that the model performs well on the training data, but does not generalize well.

- Overfitting happens when the model is too complex relative to the amount and noisiness of the training data.

The possbile solutions are : 

1) To simplify the model by selecting one with fewer parameters (linear than polynomial), by reducing the number of attributes in the training data or by constraining the model.

2) To gather more training data
   
3) To reduce the noise in the training data (e.g. fix data errors and remove outliers)


- **Regularization** : constraining a model to make it simpler and reduce the risk of overfitting
- e.g.) we have $\theta_1$ and $\theta_0$ for the parameters of our linear model. This gives the learning algorithm **two degrees of freedom** to adapt the model to the training data. If any of the parameters are forced to be 0, that would be one degree of freedom.

- We would want to keep this model simply and fit the data perfectly for good generalization.

- We can see how regularization makes the model fit a bit less to the training data, but generalize better. Hence, reducing the risk of overfitting.


<h3>Underfitting the Training Data</h3>

- This happens if your model is too simple to learn the underlying structure of the data.

Options to fix this problem :

1) Selecting a more powerful model, with more parameters
2) Feeding better features to the learning algorithm (feature engineering)
3) Reducing the constraints on the model (reducing the regularization hyperparameter)


<h3>Basic Summary of ML</h3>

1) ML is about making machines get better at some task by learning from data, instead of having to explicitly code rules.

2) There are many different types of ML : supervised/unsupervised, batch/online, instance/model based

3) We feed the training dataset to a learning algorithm. If this is model-based, it tunes some parameters to fit the model to the training set. If it is instance-based, it just uses similiarity measure to generalize to new instances.

4) The system will not perform well if the training set is too small, biased, not representative, noisy, or polluted with outliers or irrelevant data.




