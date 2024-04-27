- can we build a leetcode problems recommendation system using the user stats and his/her recent submissions ?

  - Goal is to recommend a list of questions from Leetcode based on user's recent submissions (20) and user's contest stats and other relevant stats on Leetcode platform.

  1. write a script to collect the User data from Leetcode GraphQL API --> **DONE**
  2. Create a dataset of Leetcode problems and it's attributes --> Figure the best dataset considering the data quality such that it can determine the recommendations most accurately
  3. identify the features or the keys from the json response which can act as potential features for the recommendation model
  4. How can we leverage the source of truth ( gathered dataset ) to map to user's recent problems ? --> This requires some thought and coding maybe ? Think about it more
  5. 3 will be part of the recommendation system  core logic ?
  6. how can I use an LLM or LLM Function Calling here ? is it worthy giving a thought in this direction ? dont heavily depend on prompt engineering
- try to modular code with clear separation of concerns
