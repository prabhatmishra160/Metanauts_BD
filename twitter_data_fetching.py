#!/usr/bin/env python
# coding: utf-8

# In[97]:


import tweepy
import pandas as pd


# In[85]:



API_key=""

API_secret=""


# In[86]:



access_token=""


access_token_secret=""


# In[101]:


# connected to jump server of twitter
auth=tweepy.OAuthHandler(API_key,API_secret)
# now we can connect from jump server to web server of twitter
auth.set_access_token(access_token,access_token_secret)
# now we can connect to API storge server of twitter
api=tweepy.API(auth)


# In[108]:


cursor=tweepy.Cursor(api.user_timeline, id='JoeBiden',tweet_mode="extended").items(100)


# In[109]:


print(cursor)


# In[ ]:


number_of_count=200
likes=[]

times=[]
tweets=[]

for i in tweepy.Cursor(api.user_timeline,id="realDonaldTrump",tweet_mode="extended").items(number_of_count):
    tweets.append(i,full_text)
    likes.append(i,favorite_count)
    times.append(i,created_at)
 


# In[30]:


cursor=tweepy.Cursor(api.user_timeline,id="realDonaldTrump",tweet_mode="extended").items()


# In[31]:


cursor


# In[ ]:





# In[ ]:




