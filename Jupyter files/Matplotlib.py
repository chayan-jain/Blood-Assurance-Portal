
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[5]:


h = [2,4,6,8,10]


# In[6]:


p = [20,40,60,80,100]


# In[33]:


plt.plot(h,p,'r*--',color='#552255',lw=2,marker='o',markersize=40,markerfacecolor='#ff0000')
plt.xlabel('hrs')
plt.ylabel('Percentage')
plt.title('Marks')
plt.show()  # When run on command line it needed.


# In[34]:


plt.scatter(h,p)


# In[35]:


import seaborn as sns


# In[36]:


tips = sns.load_dataset('tips')


# In[37]:


tips.head(5)


# In[44]:


sns.distplot(tips['total_bill'],kde=False,bins=30)


# In[48]:


plt.scatter(tips['total_bill'],tips['tip'])


# In[47]:


sns.jointplot(x='total_bill',y='tip',data=tips)


# In[49]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[50]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[51]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[54]:


sns.pairplot(tips,hue='sex',palette='coolwarm')


# In[55]:


sns.barplot(x='sex',y='total_bill',data=tips)


# In[56]:


sns.boxplot(x='sex',y='total_bill',data=tips)


# In[57]:


sns.boxplot(x='sex',y='total_bill',data=tips,hue='smoker')


# In[58]:


sns.violinplot(x='day',y='total_bill',data=tips)


# In[59]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker')


# In[60]:


sns.swarmplot(x='day',y='total_bill',data=tips,hue='smoker')


# In[1]:


import plotly  #  We need net for plotting graph


# In[62]:


import cufflinks as cf


# In[63]:


from plotly.offline import download_plotlyjs,init_notebook_mode,iplot


# In[64]:


init_notebook_mode(connected=True)


# In[65]:


cf.go_offline()


# In[66]:


import pandas as pd


# In[67]:


import numpy as np


# In[75]:


df = pd.DataFrame(np.random.randn(100,4),columns=['a','b','c','d'])


# In[77]:


df.plot()


# In[78]:


df.iplot()   # It will highlight the points


# In[79]:


df.iplot(kind='scatter',x='a',y='b',mode='marker')


# In[80]:


df.iplot(kind='surface',colorscale='rdylbl')


# In[81]:


df.iplot(kind='surface')


# In[82]:


df.iplot(kind='bubble',x='a',y='b',size='c')

