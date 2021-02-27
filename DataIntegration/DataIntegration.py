#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pandera as pa
import numpy as np


# In[2]:


acs = pd.read_csv("acs2017_census_tract_data.csv")
covid = pd.read_csv("COVID_county_data.csv")
acs.shape
n = len(pd.unique(acs['County']))
print(n)


# In[3]:


covid.head()


# In[4]:


from scipy import integrate
acsgrouped = acs.groupby(['County', 'State'], as_index=False)['TotalPop'].sum()
acsgrouped.head()
# acsgrouped.shape


# In[7]:


acs_agg = acsgrouped[['County','State', 'TotalPop']]
acs_agg.head()


# In[ ]:





# In[ ]:




