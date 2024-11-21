#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("E:/Machine_Learning_by_Aditya_Sir/Expanded_data_with_more_features.csv")
df=df.drop("Unnamed: 0", axis = 1)
print(df.head()) # call first 5 columns with rows


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


df.isnull().sum()  # we got not null values which column contain the null values


# In[23]:


df


# # Gender Distribution

# In[11]:


plt.figure(figsize=(6,5))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()


# # from the above chart we have analysed that the number of females in the data is more than the number of males
# 

# In[12]:


gb=df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[13]:


plt.figure(figsize=(6,6))
sns.heatmap(gb,annot=True)
plt.title("Relationship b/t Parent's Education and Student's Score")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()


# # from the above chart we conculuded that the education of the Parents have a good impact on their scores

# In[14]:


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)


# In[51]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot=True)
plt.title("Relationship b/t Parent's Marital Status and Student's Score")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()


# # from the above chart we have concluded that the there is no/eligible impact on the student's score due to their Parent's Marital Status

# In[15]:


sns.boxplot(data=df,x="MathScore")
plt.show()


# In[16]:


sns.boxplot(data=df,x="ReadingScore")
plt.show()


# In[17]:


sns.boxplot(data=df,x="WritingScore")
plt.show()


# In[18]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Group

# In[20]:


groupA=df.loc[(df['EthnicGroup']=="group A")].count()
groupB=df.loc[(df['EthnicGroup']=="group B")].count()
groupC=df.loc[(df['EthnicGroup']=="group C")].count()
groupD=df.loc[(df['EthnicGroup']=="group D")].count()
groupE=df.loc[(df['EthnicGroup']=="group E")].count()

l=["group A","group B","group C","group D","group E"]
mylst=[groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
print(mylst)


plt.pie(mylst,labels=l,autopct="%1.2f%%")
plt.title("Distribution of Ethnic Group's")
plt.show()


# In[21]:


ax=sns.countplot(data=df,x='EthnicGroup')
ax.bar_label(ax.containers[0])




# In[22]:


df


# In[ ]:





# In[ ]:




