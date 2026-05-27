# Start working with Real Data (California Housing Prices)

### Data Pipeline

- A sequence of data processing components. Each component pulls in a large amount of data, processes it, and spits out the result in another data store.

- Then, of course, the next pipeline pulls in this data and spits its own output.

- With the help of a data flow graph, this makes the system simple to grasp. Different teams can focus on different components

- The architecture is quite robust since even if a component breaks down, the downstream components can continue to run normally by just using the last output of the broken one

- But, we still need proper monitoring for the breaking components
