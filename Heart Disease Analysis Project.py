#!/usr/bin/env python
# coding: utf-8

# # 1. Importing the required dataset

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


d=pd.read_csv("D:\\Datasets\\heart.csv")


# In[7]:


df=pd.DataFrame(d)


# In[9]:


df


# # 2. Display top 5 rows of the dataset

# In[11]:


df.head()


# - age
# - sex
# - chest pain type
#     - Value 0:typical angina
#     - Value 1: atypical angina
#     - Value 2: non-anginal pain
#     - Value 3:asymptomatic
# - trestbps: resting blood pressure(in mm Hg on admission to the hospital)
# - chol: serum cholestral in mg/dl
# - fbs: (fasting blood sugar > 120 mg/dl)(1=true,0=false)
# - restecg: resting electrocardiographic results
#     - value 0:normal
#     - value 1:having ST-T wave abnormally (T wave inversions and/or ST             elevation or depression of > 0.05 mV)
#     - value 2:sgowing probable or definite left ventriculat=r hypertrophy by Estes' criteria
# - thalach: maximum heart rate achieved
# - exang: exercise induced angina (1=yes,0=no)
# - oldpeak = ST depression induced by exercise relative to rest
# - slope: the slope of the peak exercise ST segment
#     - Value 1: unsloping
#     - Value 2: flat
#     - Value 3: downsloping
# - ca: number of major vessels (0-3) colored by flouroscopy
# - thal: 3=normal, 6=fixed defect,7=reversible defect
# - target: 0=less chance of the heart attack, 1=more chance of heart attack

# # 3. Check last 5 rows of the dataset

# In[12]:


df.tail()


# # 4. Find the shape of the dataset

# In[15]:


a=df.shape


# In[16]:


print("Number of rows =",a[0])
print("Number of columns=",a[1])


# # 5. Get information about dataset like total number of rows, total number of columns, datatypes of each column and memory requirement

# In[17]:


df.info()


# # 6. Check NULL values in the dataset

# In[19]:


df.isnull().sum()


# # 7. Check for the duplicate data and drop them

# In[24]:


data_dup=df.duplicated().any()
print(data_dup)


# In[25]:


df.drop_duplicates(inplace=True)


# In[26]:


df.shape


# # 8. Get overall statistics of the dataset

# In[27]:


df.describe()


# # 9. Draw correlation matrix

# In[30]:


plt.figure(figsize=(17,6))
sns.heatmap(df.corr(),annot=True)


# # 10. How many people have heart disease, and how many don't have heart disease in this dataset

# In[31]:


df.columns


# In[34]:


df['target'].value_counts()


# In[47]:


sns.countplot(x='target',data=df)
plt.show()


# # 11. Find the counts of male and female in this dataset

# In[40]:


df.columns


# In[42]:


df['sex'].value_counts()


# In[48]:


sns.countplot(x='sex',data=df)
plt.xticks((1,0),('Male','Female'))
plt.show()


# # 12. Find the gender distribution according to the target variable

# In[49]:


df.columns


# In[56]:


sns.countplot(x='sex',hue='target',data=df)
plt.xticks((1,0),('Male','Female'))
plt.legend(['No disease','disease'])
plt.show()


# # 13. Check age distribution in the dataset

# In[57]:


df.columns


# In[72]:


sns.distplot(df['age'],bins=20)
plt.show()


# # 14. Chest pain type

# - chest pain type
#     - Value 0:typical angina
#     - Value 1: atypical angina
#     - Value 2: non-anginal pain
#     - Value 3:asymptomatic

# In[73]:


df.columns


# In[79]:


sns.countplot(x='cp',data=df)
plt.xticks([0,1,2,3],['typical angina','atypical angina','non-anginal pain','asymptomatic'])
plt.xticks(rotation=75)
plt.show()


# # 15. Show the chest pain distribution as per the target variable

# In[80]:


df.columns


# In[87]:


sns.countplot(x='cp',hue='target',data=df)
plt.legend(labels=['No disease','disease'])
plt.show()


# # 16. Show fasting blood sugar distribution according to the target variable

# In[88]:


df.columns


# In[89]:


sns.countplot(x='fbs',hue='target',data=df)
plt.legend(labels=['No disease','disease'])
plt.show()


# # 17. Check resting blood pressure distribution

# In[90]:


df.columns


# In[92]:


df['trestbps'].hist()
plt.show()


# # 18. Compare resting blood pressure as per sex column

# In[93]:


df.columns


# In[100]:


g=sns.FacetGrid(df,hue='sex',aspect=4)
g.map(sns.kdeplot,'trestbps',shade=True)
plt.legend(labels=['Male','Female'])
plt.show()


# # 19. Show distribution of Serum Cholesterol

# In[101]:


df.columns


# In[103]:


df['chol'].hist()
plt.show()


# # 20. Plot continuous variables

# In[104]:


cat_values=[]
cont_values=[]
for i in df.columns:
    if df[i].nunique() <=10:
        cat_values.append(i)
    else:
        cont_values.append(i)


# In[105]:


cat_values


# In[106]:


cont_values


# In[111]:


df.hist(cont_values,figsize=(15,6))
plt.tight_layout()
plt.show()


# In[ ]:




