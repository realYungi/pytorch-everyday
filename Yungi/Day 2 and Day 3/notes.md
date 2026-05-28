### Train / Test Set

- Before this, as we all know, we go through EDA

- But, if we are doing EDA, especially if we are trying to make a graph, we need to understand the units of the dependent variables and check if all the range of independent variables are covered.


- **Data Snooping Bias** : when you estimate the generalization error using the test set, your estimate will be too optimistic, and you will launch a system that will not perform as well as expected

- Remember, if we create a test set randomly, the next time we run it, it would be different. So, we can rather **set a seed**, or use each instance's identifier to decide whether it should go in the test set?