# Machine Learning
- General definition
> ML is the field of study that gives computers the ability to learn without being explicitly programmed
- Engineering-oriented
> A computer program is said to learn from experience $E$ wrt. some tasks $T$ and some performance measure $P$, if its performance on $T$, as measured by $P$, improves with experience $E$

## Importance of Machine Learning
- Compared with brittle, hand‑written rules, machine learning uses data to produce working solutions quickly and reduces the need to encode every exception by hand
- By training models on lots of data, ML shifts effort toward collecting and curating examples and can deliver better performance on complex, noisy tasks, because models can be retrained or updated automatically as data changes, ML systems can adapt continuously and scale far beyond manual rule‑fix cycles
- ML doesn't just automate, it reveals patterns and failure modes that help humans better understand the problem and improve the overall solution

## Types of Machine Learning Systems
### Training Supervision
ML systems can be classified according to the amount and type of supervision they get during training. 

**Supervised Learning**
![alt text](../../assets/image.png)
- The training set we feed to the algorithm includes labels (i.e. desired solutions)
- One such task of a typical supervised learning is *classification*. 
- Another predicts a *target* numeric value, given a set of *features*. We calll this specific task *regression*, so to train the system, we need to give it many examples of data, including both their features and targets
    - *logistic regression* is commonly used for classification, as it can output a value that corresponds to the probability of belonging to a given class

**Unsupervised Learning**
- The training data is unlabeled, so the system tries to learn without guidance
- Tasks of unsupervised learning include clustering, dimensionality reduction, visualization, and anomaly detection.

### Visualization (t-SNE / embedding methods)
- Visualization algorithms (for example t-SNE or UMAP) project high‑dimensional data into 2D or 3D so humans can inspect structure. These projections often reveal semantic clusters (for example animals vs vehicles) that help you understand what features the model can exploit.

![t-SNE visualization](../../assets/tsne.png)
*Figure: Example of a t‑SNE embedding showing semantic clusters.*

### Anomaly detection
- Anomaly detection learns the distribution of mostly normal training instances and flags new points that fall far from that distribution. This is useful for fraud detection, manufacturing defects, or removing outliers before training another model.

![Anomaly detection](../../assets/anomaly.png)
*Figure: Anomaly detection distinguishes normal instances from outliers.*

### Semi‑supervised learning
- Semi‑supervised methods use a few labeled examples together with many unlabeled ones. By leveraging the structure in the unlabeled data (for example clusters), these methods can propagate labels and improve performance when annotations are scarce.

![Semi-supervised learning](../../assets/semi_supervised.png)
*Figure: Semi‑supervised learning — unlabeled examples help classify new instances.*

### Self‑supervised learning
- Self‑supervised learning creates pseudo‑labels from unlabeled data (for example, by masking parts of an image and training the model to reconstruct them). These pretraining tasks produce representations that can be fine‑tuned for downstream tasks and support transfer learning.

![Self-supervised learning](../../assets/self_supervised.png)
*Figure: Self‑supervised example — mask and reconstruct to learn useful representations.*

### Reinforcement learning
- Reinforcement learning trains an agent to choose actions that maximize long‑term reward by interacting with an environment. It is the right paradigm for sequential decision problems such as robotics, game playing, and recommendation systems that must optimize over time.

![Reinforcement learning](../../assets/reinforcement_learning.png)
*Figure: Reinforcement learning — agent observes, acts, receives rewards, and updates a policy.*

# Appendix
- **training set**: A collection of examples used to train a model. In supervised learning each example typically includes input features and a label (target).
- **training instance (sample)**: A single example from the training set. It contains input feature values and, for supervised tasks, an associated label.
- **feature**: An individual measurable property or attribute of an instance (for example, pixel values, word counts, or sensor readings).
- **label (target)**: The ground‑truth value or desired output used for supervised training (for example a class name or numeric target).
- **model**: A parameterized function learned from data that maps inputs (features) to outputs (predictions); training adjusts the model's parameters to improve performance on the task.
- **validation set / test set**: Held‑out data used to tune hyperparameters (`validation`) or to estimate final performance (`test`) without influencing training.