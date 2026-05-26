# Instance-Based VS Model-Based Learning

- One more way to categorize ML systems is by how they **generalize**

- Given number of training examples, the system needs to be able to generalize to examples it never seen before.
- We need to find a way so that the system performs well on new instances

Two main approaches to generalization: instance-based learning / model-based learning

<br>

<h3>Instance-based Learning</h3>

- For example, for spam email filtering, we not only identify identical emails to the spam emails, but also flag emails that are very similar to known spam emials.

- Hence, this requires a **measure of similarity** between two emails. So, a system would flag an email as spam if it has many words in common with a known spam email.

- Instanced-based Learning : the system learns the examples by heart and generalizes to new cases using a similarity measure.
- This often works well with small-datasets.
- Does not work well with high dimension data like images as finding similar instances may take slow time.

<br>

<h3>Model-based Laerning</h3>

- Another way to generalize is to generalize from set of examples to build a model of these, then use that model to make predictions.

- e.g.) We want to know if money makes people happy. So, we load the *Better Life Index* data and GDP per capita. Then, we can know countries' life satisfaction depending on their GDP. We plot that data, find the trend and find the pattern / correlation of the model.

- Linear model is a good example of this, thus linear regression would be a good thing to consider.

- The part where we select a model (whether that be linear, polynomial) = **model selection**

- For models, we need to determine which values of the parameters of the models perform the best. Here, we use the **utilitiy function** or the **fitness function** that measures how good the model is.
- Or, conversely, we can use a **cost function** to measure how bad the model is.

- Linear Regression model, usually uses cost function that measures the distance the linear model prediction and the training examples, and minimizes that distance to find the best fit.

- The process of finding the best fit would be called **training** the model. (when the loss function where we minimize the distance in case of linear regression)

<br>

<h3>Extra: When to use Instance Based and Model Based Learning</h3>

- Review: instance based learning predicts the outcome by using similarity measures
- And model based learning predicts the outcomes using a model that fits well to the current data point, representing its trend.

- Use instance based learning if we need a quick flexible system without building too much of a complex formulas
- Use model based if you actually want the system to actually "learn" underlying rules and generalize to unseen data.

<br>

<h3>Summary</h3>

- You study the data
- You select a model
- You train it using training data (learning algorithm searched for the model parameter values that minimize the cost function)
- Apply the model to make predictions on new caes (inference) hoping that this model will generalize well.












