#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
listings=pd.read_csv('listings.csv')
plt.hist(listings['price'],bins=np.arange(0,1100,80))
plt.xlabel('price(in US Dollars)')
plt.ylabel('no.of barrels')
plt.show()


# In[17]:


sn.barplot(x='neighbourhood_group',y='price', data = listings,ci = False)
plt.show()


# In[20]:


plt.scatter(x=listings['price'],y=listings['number_of_reviews'],s=5)
plt.xlabel('price')
plt.ylabel('number_of_reviews')
plt.xlim(0,1100)
plt.show()


# In[7]:


df=pd.read_csv('listings.csv')
ab=df.head()
x=ab["name"]
y=ab["price"]
plt.pie(y,labels=x,radius=1.2,shadow=True)
plt.show()


# In[17]:


ab.boxplot(by ='room_type', column =['price'], grid = False) 


# In[25]:


baby_names=pd.read_csv('us_baby_names.csv')


# In[26]:


baby_names


# In[27]:


baby_names.head()


# In[37]:


ap=baby_names.head()
ad=ap.corr()
print(ad)


# In[36]:


hm = sn.heatmap(data=ad,cmap="RdYlGn",annot=True) 
plt.show() 

