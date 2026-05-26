# Batch and Online Learning

- Another criterion used to classify ML systems is whether or not the system can learn incrementally from a stream of incoming data

<h3>Batch Learning : Something like random forests</h3>

- Here, the system is incapable of learning incrementally, so it must be trained using all the available data. This takes up a lot of time and computing resources, so it is typically done offline.

- The system is trained first, launched into production, and runs without learning anymore.

- It just applies what it has learnt before. No more updates, solely uses the knowledge it has.

- If we want a batch learning system to know about new data, we need to train the whole thing again, stop the production of the old one, and replace with the new one.
- The pros of this approach is that it is accurate and reliable. But, of course, the cons would be that it requires a lot of computing resources and time.


<h3>Online Learning : Something like gradient descent</h3>

- Here, you train the system incrementally by feeding it data instances sequentially, either individually or by small groups called **mini-batches**. Each learning step is fast and cheap, so the system can learn about new data as it arrives.

- So, if we have limited computing resources, this might be a good fit. Once an online learning system learned the new data, it does not need them anymore, so you can just discard them, which saves a lot of space.

- Online Learning Algorithms can also be used to train systems on huge datasets that cannot fit in one machine's main memory. (out-of-core learning). So, the machine runs a traning step on a part of the data, runs, and repeats until it has run all of the data.

**Learning Rate** : How fast online learning systems should adapt to changing data

- If we set a high learning rate, then your system will adapt to new data fast, while also tending to quickly forget the old data. **(catastropic forgetting)**

- Conversely, if you set a low learning rate, it will learn a bit slowly, but it will also be less sensitive to noise in the new data or to sequences of nonrepresentative data points.

- Challenge of online learning : if bad data is fed, the system's performance will gradually decline. So, in this case, we need to monitor our system closely. (Switching learning off when there is a drop in performance).
