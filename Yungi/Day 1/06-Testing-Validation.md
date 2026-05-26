# Testing and Validating

- We can know how well the model generalizes by trying it on new cases. We put the model in production and monitor how well it performs.

- But, if the users' first impression is a bad model, it is too late.

- A better method would be to split our dataset into **training and test datasets**.

- The error rate on new cases is called **generalization error**. (out of sample error) This tells us how well our model will perform on instances it has never seen before.

- If training error is low, but generlization error is high, this means our model is overfitting.

- So, we use test data to evaluate our model.

- Suppose we have two models to compare: linear and polynomial model. Suppose the linear model generalizes better, but you want to apply some regularization to avoid overfitting. Question is : **how do you choose the value of the regularization hyperparameter?**

- One option is to train 100 different models using 100 different values for this hyperparameter. Let's say we found the best one, had 5% generalization error, so you launch the model, but produces 15% error in the real world.

- It's because the model and hyperparameters were adapted solely for the testing set.

- The common solution to this is to have a second holdout set called the **Validation Set**.

- **Cross-Validation** : The training set is split into complementary subsets, and each model is trained against a different combination of these subsets and validated against the remaining parts.


<h3>Extra: No Free Lunch Theorem</h3>

- When we are simplifying our data, we must make assumptions. For example, a linear model makes the assumption that the data is fundamentally linear and that the distance between the instances and the straight line is just noise, which can be ignored.

- There is no model that is a priori guaranteed to work better. The only way to know is to evaluate them all.
- In real life, this is not possible, so we have to make reasonable assumptions.
