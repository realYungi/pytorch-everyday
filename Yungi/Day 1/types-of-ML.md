# Types of Machine Learning Systems

<br>

<h2>Training Supervision</h2>

1) Supervised Learning

- Here, the training set you feed to the algorithm includes desired solutions, called <b>labels</b>
- e.g.) Typical supervised learning task : Spam Filter where we feed the model "labeled" data with distinct "class" (spam,ham)
- Another typical task : predicting a target numeric value using their features. (Regression)

<br>

2) Unsupervised Learning

- e.g.) Clustering algorithms : detecting distinct "groups" within the dataset based on their similarity
- Visualization algorithms : feed complex unlabeled data, and outputs 2D/3D representation of the data. We can understand the unsuspected patterns of this data.

- Dimensionality Reduction : simplifying the data without losing too much information. We can merge correlated features into one. (This is called feature extraction)

- Anomaly detection : machine gets trained with normal messages, and if new pattern arises, they see if the new one is similar to the normal ones, and if not, anomaly is detected.

- Association Rule Learning : dig large amounts of data and discover interesting relations between attributes (features)


<br>

3) Semi-Supervised Learning

- well, labeling data is usually time-consuming and costly, so we may have unlabeled instances, or few labeled instances. Some algorithms can deal with data that's partially labeled.

- for example, the google photos classifies human faces for us, but we are the ones who need to label their names.

<br>


4) Self-supervised Learning

- Another approach to machine learning involves generating a fully labeled dataset from a fully unlabeled one.
- once the data is labeled, a supervised learning algorithm can be used.
- this can be used to repair damaged images or to erase unwanted objects from pictures.
- But, you can fine tune your model depending on which results you would want.


<h2>Reinforcement Learning</h2>

- We have a learning system called the agent in this context, which can observe the environment, select and perform actions, and get rewards in return (or penalties in the form of negative rewards.

- Then it learns by itself what is the **best strategy**, called **policy**.

- Policy helps the agent to get the most reward over time. 

















