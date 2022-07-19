#!/usr/bin/env python
# coding: utf-8

# ## Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.
# 
# Use pandas to create a Series named fruits from the following list:
# 
# 
#     ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# In[2]:


import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.

# In[3]:


fruits.count()


# 2. Output only the index from fruits.

# In[7]:


fruits


# In[8]:


fruits.index


# 3. Output only the values from fruits.

# In[11]:


fruits.values


# 4. Confirm the data type of the values in fruits.

# In[14]:


fruits.values.dtype


# 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

# In[15]:


fruits.head()


# In[16]:


fruits.tail(3)


# In[21]:


import numpy as np
def rand_from_series(n):
    '''
    rand_from_series takes in a pd.Series
    and returns a random integer corresponding to an index
    NOTE: this will not work if the index is made of non_integers
    '''
    x = n.count() # get the count from the series
    return np.random.randint(0,x) # return a random integer between 0 and the count of the series
    


# In[57]:


rand_from_series(fruits)


# In[70]:


rfs = rand_from_series


# In[75]:


fruits[rfs(fruits)], fruits[rfs(fruits)]


# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.

# In[67]:


fruits.describe()


# 7. Run the code necessary to produce only the unique string values from fruits.

# In[76]:


fruits.unique()


# 8. Determine how many times each unique string value occurs in fruits.

# In[83]:


fruits.value_counts()


# 9. Determine the string value that occurs most frequently in fruits.

# In[89]:


fruits.value_counts().index[0]


# 10. Determine the string value that occurs least frequently in fruits.

# In[94]:


fruits.value_counts().index[-1]

