# CodeJam2017

We will break up the repository as follows 

Prelimenary stage: 
  1. Use already computed indices --> parse them --> output data structure containing a sorted list of tuples containing a country and its      index value. Create a script for this that can be imported as a module, and that we can use in a main script. Assume that if we a          country's index could not be computed due to a lack of data, then we will assign its index a value of 0.  
  2. Use input from 1. and generate a colored map. This involves generating a color scheme from 0 to 1, figuring out how to identify the        countries from a map, and fill in their respective areas without a color corresponding to the index value. 

Secondary stage: 
  1. Compute a user-requested index. The user will use a front end application (described later on) to identify metrics they are interested in, as well as the weights they'd like to assign to each metric. Note that different metrics have different ways of being processed (like life expectancy vs. child mortality rate), and we should limit the number of metrics the user can choose from to some limited number (and increase the number of metrics later on). Ideally choose a variety of metrics, that need to be treated differently to show data usage prowess. 
 2. Map generation would remain relatively constant from Prelimenary stage part 2. A bonus would be to hover over a country and see its data and rank in a bubble of sorts (so make the map interactive). 
 3. UI- Allow user to request for a map to be generated, and allow them to enter choices of metrics plus weights assigned to each metric.     This UI would return a map (potentially interactive). 
      
