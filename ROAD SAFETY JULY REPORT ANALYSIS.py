#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('C:/Users/ISRAEL/Documents/REPORT FOLDER/DUTY ROOM JULY 2019 MONTHLY REPORT.xlsx', header=None)
headers=['OFFENCES','WEEK 1','WEEK 2','WEEK 3','WEEK 4','WEEK 5','WEEK 6']
data.columns=headers
data=data.drop([0,28,32,29,31,30,8,1,2,3,4,5,6,9,7,33], axis=0)
data=data.drop(['WEEK 6'],axis=1)
data.index=data.OFFENCES
data.fillna(0)
get_ipython().run_line_magic('matplotlib', 'inline')
data.plot(kind='bar', figsize=(10,10))


# In[ ]:




