#!/usr/bin/env python
# coding: utf-8

# # <center> Construction Suppliers Analysis</center> 
# 
# ## Table of content
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# <li><a href="#Assumptions">Conclusions</a></li> 
# </ul>

# <a id='intro'></a>
# ## Introduction
# We are going to assume **Construction Suppliers data frame** is a weekly records of construction material supplied to a given company that is currently doing construction.
# 
# <p>The company is interested in knowing location of most of their suppliers,what they supplied and the challeges they had faced, in order to determine the improvements they need to make for the next month supplies.</p>
# 
# <br>**Our dataframe Contain the fllowing the attributes**</br>
# - **Company Name** -Name of the company that made the supply.
# - **Address** -Address of the company.
# - **Location** - The town where the company is located.
# - **Email address** -The company contact.
# - **Phone Number** - Company contact number.
# - **Supplied Item** - The item or service that was provided by the company.
# - **Challenges Faced ** - Some of the problems the company faced durng the supply of the item procured from them.

# <a id='intro'></a>
# ## Exploratory Data Analysis
# 
# Our data is clean and do not need much cleaning, we just go a head and explore it.
# - The **NaN** in the column of *challeged_face* of our data means *none* and it is important record in this type of data frame,therefore we are not going to drop them.

# In[1]:


#import the packages to be used for our analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy.stats as stats
sns.set_style('darkgrid')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# In[11]:


#load the dataset be used for the analysis
df=pd.read_excel('Construction suppliers.xlsx')

#view the top data,since our dataframe is a bit huge,
#we load the top five record to check if the dataframe was loaded correcly.
df.head(10)


# In[3]:


#let get the size of our data to see if the whole dataframe was uploaded to our work space
df.shape


# **Our data frame contain 60 colums(Companies) and 7 rows(Attributes)**

# In[4]:


#Lets find the summary of all columns the with their data types and 
#and including the number of non-null values in each column.
df.info();


# ### Location Analysis

# In[5]:


#let find the top most five locations(town) that the suppliers were from
top_location=df['Location'].value_counts()[:5]
top_location.head()


# **Most of the suppliers of this month were from Nairobi town**

# In[6]:


#Lets plot pie chart representation of the supply towns
#it will help us see the distribution of the towns in comparison with the top 5 towns
df[df['Location'].notnull()]['Location'].value_counts().plot(kind = 'pie', autopct='%1.1f%%')
plt.title('Top Suppliers Town')


# ### Supplied Items analysis

# In[7]:


#let find out the most supplied items this month
#the result will help us also how many companies supplied the same items
supplied_items=df['Supplied_item'].value_counts()
supplied_items


# ### Interpretation
# - From th e result we can say,this weeks contruction plan required more of Timber,Ballast,river,Cement and building of the perimeter walls,therefore supply tender was given to more than three companies.

# ### Challeges Faced  Analysis

# In[8]:


#Let find the occurances of challenges the suppliers faced
challenges_faced=df['Challenges_faced'].value_counts()
challenges_faced


# ### Interpretation
# - From our analysis above,most of the suppliers faced the challeges of delayed payments after they had made the supply and over quotation which always means that the competition was high.

# In[9]:


#let check the distribution on a bar graph
challenges_faced.plot(kind ='bar',title='challenges suppliers faced',x='Location', y='count', figsize= (10,7))


# In[10]:


#lets find the number number of suppliers who never faced any challege
df['Challenges_faced'].isna().sum()


# ### Interpretation
# - The number of suppliers who never faced any challege is the highest, though it does not give the accurate picture because the reson why  some suppliers never faced any challege is because they did not participaate in the project in the first place and it is not easy to tell from the way this data frame was captured**

# ## Conclusion 
# 
# - This week most of the suppliers were from Nairobi town.
# - Due to lack of proper planning by the procurement department,most of the suppliers were not paid on time,though we can proudly say a good number of them did well and did not face any challege at all.
# - Over quatation of the market prices can also be a big issue to make supplier lose their supply contract,thefore it is advisable to do a proper market research before enlisting you product prices.
# 

# ## Assumption
# - The dataframe used is assumed to present a company procurement project award record to the different supplies for a peiod of one week. 
# - The null value under *challeges_faced* column is asumed to mean that the supplier did not face any challege by either,completion of the project and paid on time or did not show up completely after they were awarded the project.
# 

# In[ ]:




