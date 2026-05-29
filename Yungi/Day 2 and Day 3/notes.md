### Train / Test Set

- Before this, as we all know, we go through EDA

- But, if we are doing EDA, especially if we are trying to make a graph, we need to understand the units of the dependent variables and check if all the range of independent variables are covered.


- **Data Snooping Bias** : when you estimate the generalization error using the test set, your estimate will be too optimistic, and you will launch a system that will not perform as well as expected

- Remember, if we create a test set randomly, the next time we run it, it would be different. So, we can rather **set a seed**, or use each instance's identifier to decide whether it should go in the test set?

- They say that changing PYTHONHASHED = 0 in the environment before using python may help, but I don't know if this is necessary.

- **Scikit-Learn** has train_test_split(), where it generates seed for us, so I guess we can just use that

### Sampling Bias

- When we have large sample of data, random sampling is fine. However, in small datasets, there would be a sampling bias

- The sample should be the representative of the "whole" population.

- **Stratified Sampling** : The population is divided into homogeneous subgroups called "strata" and the right number of instances are sampled from each stratum to guarantee that the test set is representative of the overall population

