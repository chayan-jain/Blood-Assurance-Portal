
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:





# In[6]:


df = np.random.randint(0,100)
raw_data = {
            'Date':[i for i in range(1,31)],
            'O+': [np.random.randint(50,70) for i in range(30)],
            'O-': [np.random.randint(60,80) for i in range(30)],
            'A+': [np.random.randint(40,70) for i in range(30)],
            'A-': [np.random.randint(30,60) for i in range(30)],
            'B+': [np.random.randint(50,80) for i in range(30)],
            'B-': [np.random.randint(60,80) for i in range(30)],
            'AB+': [np.random.randint(50,80) for i in range(30)],
            'AB-': [np.random.randint(60,90) for i in range(30)],
            'HH': [np.random.randint(0,10) for i in range(30)],
    }
df = pd.DataFrame(raw_data, columns = ['Date','O+', 'O-', 'A+', 'A-', 'B+','B-','AB+','AB-','HH'])
df.to_csv(r'C:\Users\Prateek\Desktop\Ansible\Project\BloodGroupDataset\temp.csv')
print("Blood group dataset is created.")
df


# In[21]:


plotDf = df.head(5)
sns.distplot(plotDf['O+'],kde=False,bins=30)


# In[22]:


plt.scatter(df['O+'],df['O-'])


# In[23]:


sns.jointplot(x=df['AB+'],y=df['AB-'],data=df,kind='hex')


# In[27]:


plotDf = df.tail(15)
sns.pairplot(plotDf,palette='coolwarm')


# In[26]:


sns.jointplot(x=df['AB+'],y=df['AB-'],data=df,kind='reg')


# In[25]:


sns.barplot(x=df['AB+'],y=df['AB-'],data=df)


# In[24]:


sns.swarmplot(x=df['AB-'],y=df['HH'],data=df)


# In[123]:


sns.barplot(x=df['O-'],y=df['HH'],data=df)


# In[17]:




