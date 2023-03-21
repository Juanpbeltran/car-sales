#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


url = "C:\\Users\\jp\\Downloads\\auto-mpg .xlsx"
df = pd.read_excel(url)


# In[6]:


df.head()


# In[7]:


df.isnull().sum()


# In[8]:


df['acceleration'] = df['acceleration'].fillna(df['acceleration'].mean())


# In[9]:


df['model year'] = df['model year'].fillna(df['model year'].mode())


# In[ ]:





# In[10]:


df.isnull().sum()


# In[11]:


df.dtypes


# In[12]:


df = df.drop_duplicates(subset='CAR Number', keep="first")


# In[13]:


#Display the first five and last five rows, Display all the column names in the dataset , Display the concise summary of your dataset, Display the name of the car with maximum number of horsepower.
df.head(5)


# In[14]:


df.tail(5)


# In[15]:


df.columns


# In[16]:


df. describe, df.axes,df.ndim, df.size, df.shape


# In[17]:


df["horsepower"].max()


# In[18]:


df["horsepower"].value_counts()


# In[19]:


df.loc[df['horsepower']==df['horsepower'].max(), 'car name']


# In[20]:


df["mpg"] = 235/df["mpg"]

# rename column name from "highway-mpg" to "highway-L/100km"
df.rename(columns={'mpg':'L/100km'}, inplace=True)

# check your transformed data 
df.head()


# In[21]:


df['weight'] = df['weight']/df['weight'].max()
df.head()


# In[22]:


bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins


# In[23]:


group_names = ['Low', 'Medium', 'High']


# In[62]:


df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)


# In[24]:


import matplotlib as plt
from matplotlib import pyplot
# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# In[25]:


import seaborn as sns
#
# Box plot
#
sns.boxplot(df.horsepower)
#
# Distribution plot
#
sns.distplot(df.horsepower)


# In[26]:


mean = df['acceleration'].mean()
std = df['acceleration'].std()

print('mean of the dataset is', mean)
print('std. deviation is', std)

threshold = 3
outlier = []
for i in df['acceleration']:
    z = (i-mean)/std
    if z > threshold:
        outlier.append(i)
print('outlier in dataset is', outlier)


# In[28]:


echo "# car-sales" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Juanpbeltran/car-sales.git
git push -u origin main


# In[ ]:




