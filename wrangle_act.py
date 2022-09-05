#!/usr/bin/env python
# coding: utf-8

# # Project: Wrangling and Analyze Data

# ## Data Gathering
# In the cell below, gather **all** three pieces of data for this project and load them in the notebook. **Note:** the methods required to gather each data are different.
# 1. Directly download the WeRateDogs Twitter archive data (twitter_archive_enhanced.csv)

# In[2]:


import os
import pandas as pd
import numpy as np
import time
from PIL import Image
import seaborn as sb
import json
import requests
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Gathering the data

# In[3]:


# Import the twitter-archive-enhanced CSV file into a DataFrame
df=pd.read_csv('twitter-archive-enhanced.csv')


# In[4]:


#read the csv file into the working data in the informtion needed for analysis.
df.head()


# In[5]:


df.info()


# 2. Use the Requests library to download the tweet image prediction (image_predictions.tsv)

# In[6]:


#Image predictions File downloaded programmatically using the Requests library 
url= 'https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
response=requests.get(url)
#read trhough the .tsv data contents
with open('image-predictions.tsv',mode='wb') as file:
    file.write(response.content)


# In[7]:


image_predictions=pd.read_csv('image-predictions.tsv',sep='\t')


# In[8]:


#read through the downloaded  file contents
image_predictions.head()


# In[9]:


#read extra information and explore more on the available information in the image_predictions.
image_predictions.describe()


# In[10]:


df.describe()


# In[11]:


#display the needed current information loaded in the dataset under the images file.
df.info()


# 3. Use the Tweepy library to query additional data via the Twitter API (tweet_json.txt)

# In[12]:


tw=pd.read_csv('twitter-archive-enhanced.csv')


# In[13]:


import requests
url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv '
response = requests.get(url)

# Save HTML to file

with open("image_predictions.tsv", mode='wb') as file:
    file.write(response.content)


# In[14]:


#display a line of every information in using the tweet_id,status,user_id and timestamp.
df.head()


# In[15]:


#view the current information before further cleaning.
df.describe()


# In[16]:


#Reading the image_predictions of CSV
image_predictions = pd.read_csv('image_predictions.tsv', sep='\t')


# In[17]:


image_predictions.info()


# In[18]:


df.head()


# In[19]:



df.describe()


# In[20]:


#dispay value information needed for checking availability.
df.count()


# #tweet API -JASON file

# In[21]:


import tweepy
from tweepy import OAuthHandler
import json
from timeit import default_timer as timer

# Query Twitter API for each tweet in the Twitter archive and save JSON in a text file
# These are hidden to comply with Twitter's API terms and conditions
consumer_key = 'HIDDEN'
consumer_secret = 'HIDDEN'
access_token = 'HIDDEN'
access_secret = 'HIDDEN'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


# In[22]:


# Tweet IDs for which to gather additional data via Twitter's API
tweet_ids = df.tweet_id.values
len(tweet_ids)


# In[23]:


# Fetch tweets from the twitter API using the following loop:
list_of_tweets = []
# Tweets that can't be found are saved in the list below:
cant_find_tweets_for_those_ids = []
for tweet_id in df['tweet_id']:   
    try:
        list_of_tweets.append(api.get_status(tweet_id))
    except Exception as e:
        cant_find_tweets_for_those_ids.append(tweet_id)


# In[24]:


#Isolating the json part of each tweepy status object that we have downloaded and adding them all into a list
my_list_of_dicts = []
for each_json_tweet in list_of_tweets:
    my_list_of_dicts.append(each_json_tweet._json)


# In[25]:


#adding the file to txt file
with open('tweet_json.txt', 'w') as file:
        file.write(json.dumps(my_list_of_dicts, indent=4))


# In[26]:


df.head()


# PROGRAMMATIC ASSESSMENT

# 1.twitter.csv

# In[27]:


#read samples of twitter.csv file
df.head().sample(5)


# In[ ]:


#reading the archive.csv file information 
df.head().info()


# In[ ]:


#reading through descriptive data
df.head().describe()


# In[ ]:


#checking for duplicated information
df.isnull().sum()


# Image predictions

# In[ ]:


image_predictions = pd.read_csv('image_predictions.tsv', sep='\t')


# In[ ]:


#read image_predictions
image_predictions = pd.read_csv('image_predictions.tsv')


# In[ ]:


df.tail()


# In[ ]:


df.describe()


# In[ ]:


#Check duplicates in image_duplications
sum(image_predictions.duplicated())


# In[ ]:


image_predictions.isnull().sum()


# ## Assessing Data
# In this section, detect and document at least **eight (8) quality issues and two (2) tidiness issue**. You must use **both** visual assessment
# programmatic assessement to assess the data.
# 
# **Note:** pay attention to the following key points when you access the data.
# 
# * You only want original ratings (no retweets) that have images. Though there are 5000+ tweets in the dataset, not all are dog ratings and some are retweets.
# * Assessing and cleaning the entire dataset completely would require a lot of time, and is not necessary to practice and demonstrate your skills in data wrangling. Therefore, the requirements of this project are only to assess and clean at least 8 quality issues and at least 2 tidiness issues in this dataset.
# * The fact that the rating numerators are greater than the denominators does not need to be cleaned. This [unique rating system](http://knowyourmeme.com/memes/theyre-good-dogs-brent) is a big part of the popularity of WeRateDogs.
# * You do not need to gather the tweets beyond August 1st, 2017. You can, but note that you won't be able to gather the image predictions for these tweets since you don't have access to the algorithm used.
# 
# 

# ### Quality issues
# 
#  1.There are expanded URLs from the twitter-archive data distribution which      need to be removed.
#  
# 2.In image-predictions ,retain id, retweet_counts,favourite_counts and remove the rest the of the data.
# 
# 3.from archives data, we have to remove the tweet replys rows from the dataset.
# 
# 4.from the tweet-archives remove the retweet table since we only need to view tweets from tweets.
# 
# 5.remove rows with missing links to check on data authenticity.
# 
# 6.in columns of datasets replace the Non values with np.nan.
# 
# 7.assess missing values in the twitter archive data.
# 8.Only a few columns are needed for the analysis.

# ### Tidiness issues
# #image_predictions
# 1.Change the names of columns type (p1, p2 and p3) to a more descriptive name.
# #this tidy issue is to allow on easy analysis and creating of insights in the dataset.
# 2.Replace 'None' with np.nan to indicate the missing values
# #this tidy issue checks on the issue to drop several information in the dataset tha will not be directly needed in the analysis since we are only interested in the dog breeds mentioned in the WeRateDogs dataset.

# ## Cleaning Data
# In this section, clean **all** of the issues you documented while assessing. 
# 
# **Note:** Make a copy of the original data before cleaning. Cleaning includes merging individual pieces of data according to the rules of [tidy data](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html). The result should be a high-quality and tidy master pandas DataFrame (or DataFrames, if appropriate).

# In[29]:


# Make copies of original pieces of data
df=pd.read_csv('twitter-archive-enhanced.csv')
df.copy()


# In[30]:


pd.read_csv('image-predictions.tsv')
df.copy()


# 1.tweet_archive
# Tiddines issues

# #Tiddy issue 1.

# Replace 'None' with np.nan to indicate the missing values
# #this tidy issue checks on the issue to drop several information in the dataset tha
# will not be directly needed in the analysis since we are only interested in the dog breeds 
# mentioned in the WeRateDogs dataset.

# code

# In[31]:


# dropping unneded doggo, floofer, pupper or poppo columns
df = df.drop(['doggo', 'floofer', 'pupper', 'puppo'], axis = 1)


# # test the dataset for the cleaned tiddyness issue

# In[32]:


df.info()


# Issue #2

# Define the issue.

# #image_predictions
# Change the names of columns type (p1, p2 and p3) to a more descriptive name.

# In[74]:


# Define: rename columns 

# Code
df= df.rename(columns={'p1':'Breed_probability1', 'p2':'Breed_probability2', 'p3':'Breed_probability3'})


# In[34]:


# Test
df.head().info()


# In[ ]:





# ### Issue #1:

# #### Define:
# drop the expanded URLs from the twitter-archive-enhanced dataset

# #### Code

# In[35]:


#remove and drop expanded URL's
df=pd.read_csv('twitter-archive-enhanced.csv')
df.drop(['expanded_urls'], axis = 1)


# #### Test

# In[36]:


df.info()


# ### Issue #2:

# #### Define
# replace the Nan values in the twitter-archive-enhanced dataset

# #### Code

# In[37]:


df =  df.replace('None', np.nan)


# #### Test

# In[38]:


df.info()


# In[39]:


df_clean=df.copy


# ISSUE #3

# Define

# Define quality issue
# removing retweets from the datasets for further analysis

# code

# In[40]:


#removing retweets
df=pd.read_csv('twitter-archive-enhanced.csv')
df.drop(['in_reply_to_status_id'], axis = 1)


# Test the cleaned dataset

# #test
# df.info

# Issue #4

# Define.

# Droping the extra columns in the data gatherd in the data.

# Test

# In[41]:


#Test
#Few columns are needed for analysis
df.drop(['in_reply_to_user_id', 'retweeted_status_id','retweeted_status_timestamp' ,'retweeted_status_user_id',], axis = 1)


# #test code to assess the removed columns
# df_clean

# In[42]:


#extracting doggo, floofer, pupper,puppo from the dataset
df.drop(['doggo', 'floofer', 'pupper', 'puppo'], axis = 1)


# In[43]:


#test code
df_clean


# Issue #5

# Define

# Re-write the formart of dog names in capitalized 

# code

# In[44]:


#re-write the formart of the dog names appropriate
df['name'].str.islower().sum()


# code

# In[45]:


#capitalize the dog names in the twitter-archive-dataset
df['name'] = df.name.str.capitalize()


# Test

# In[46]:


df['name'].head()


# Issue #6

# Define

# Changing the timestamp to fit in data format

# Code

# In[47]:


#change the layout of the timestamp reading
df['timestamp'] = pd.to_datetime(df['timestamp'])


# Test

# In[48]:


#test code
df.timestamp.dtypes


# In[49]:


pd.read_csv('image-predictions.tsv')
df.head


# Issue #7

# Define

# check for data duplicates in the dataset 

# code

# In[50]:


#check for Duplicates in the csv file should be deleted.
sum(image_predictions.duplicated())


# Test for duplicates to confirm

# In[51]:


image_predictions.duplicated()


# ## Storing Data
# Save gathered, assessed, and cleaned master dataset to a CSV file named "twitter_archive_master.csv".

# In[52]:


df.to_csv('twitter_archive_master.csv',index=False, encoding = 'utf-8')


# ## Analyzing and Visualizing Data
# In this section, analyze and visualize your wrangled data. You must produce at least **three (3) insights and one (1) visualization.**

# In[53]:


df.info


# ### Insights:
# 1.The twitter-archive-dataset has a varied number of data which currently are upto date with the actual needed importance for analysis and transformatiomation.
# 
# 2.droping of duplicates from the analyzed data creates a clear impression and rating of different dog types and interpretations.
# 
# 3.null values in the data, twitter-archive-enhanced removed signify suplicity and brake down the complexity of the data.

# ### Visualization

# In[54]:


#Check for dog analysis, types and those found in the dataset
def df_plotting(df):
    df.groupby(df.image_predictions).plot(kind='bar')
    plt.show()
    df.head()


# In[55]:


df=pd.read_csv('image-predictions.tsv')
df.head()


# In[56]:


plt.show


# In[57]:


image_predictions=pd.read_csv('image-predictions.tsv',sep='\t')


# In[58]:


image_predictions.head()


# In[59]:


image_predictions.rename(columns={'p1':'first_prediction', 'p1_conf': 'first_confidence', 'p1_dog': 'first_dog',
                                  'p2': 'second_prediction', 'p2_conf': 'second_confidence', 'p2_dog': 'second_dog',
                                  'p3': 'third_prediction', 'p3_conf': 'third_confidence', 'p3_dog': 'third_dog'}, inplace = True)


# In[60]:


image_predictions.head(2)


# In[61]:


image_predictions.info()


# In[62]:


df=image_predictions.head(2)
plt.figure(figsize = (17,6))
ax = sb.barplot(x = df['first_prediction'].value_counts()[0:10].index,
            y =df['first_prediction'].value_counts()[0:10],
            data = df);
ax.set_xticklabels(ax.get_xticklabels(), fontsize = 20);
plt.xlabel("Dog Breeds",fontsize = 20);
plt.ylabel("Counts",fontsize = 20);
plt.title("WeRateDogs Breeds",fontsize = 20);


# In[63]:


df=image_predictions.head(2)
plt.figure(figsize = (17,6))
ax = sb.barplot(x = df['second_prediction'].value_counts()[0:10].index,
            y =df['second_prediction'].value_counts()[0:10],
            data = df);
ax.set_xticklabels(ax.get_xticklabels(), fontsize = 20);
plt.xlabel("Dog Breeds",fontsize = 20);
plt.ylabel("Counts",fontsize = 20);
plt.title("WeRateDogs Breeds",fontsize = 20);


# In[64]:


df=image_predictions.head(2) 
plt.figure(figsize = (17,6))
ax = sb.barplot(x = df['third_prediction'].value_counts()[0:10].index,y =df['third_prediction'].value_counts()[0:10],data = df);
ax.set_xticklabels(ax.get_xticklabels(), fontsize = 20);plt.xlabel("Dog Breeds",fontsize = 20);plt.ylabel("Counts",fontsize = 20);
plt.title("WeRateDogs Breeds",fontsize = 20);


# Insights from the datasets types of Dog breeds.

# In[65]:


#first WeRateDogsImage(Welsh_springer_spaniel)
import IPython
url = 'https://pbs.twimg.com/media/CT4udn0WwAA0aMy.jpg'
IPython.display.Image(url, width = 250)


# In[66]:


#second WeRateDogsImage(German_shepherd)
import IPython
url = 'https://pbs.twimg.com/media/CT4521TWwAEvMyu.jpg'
IPython.display.Image(url, width = 250)


# In[67]:


#third WeRateDogsImage(miniature_pinscher)
import IPython
url = 'https://pbs.twimg.com/media/CT5IQmsXIAAKY4A.jpg'
IPython.display.Image(url, width = 250)


# Stpring data

# In[68]:


#storing data to twitter_archive_master.csv file 
df.to_csv('twitter_archive_master.csv',index=False, encoding = 'utf-8')


# In[69]:


df=df.copy()


# In[ ]:





# In[ ]:




