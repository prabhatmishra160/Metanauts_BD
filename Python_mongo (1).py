#!/usr/bin/env python
# coding: utf-8

# In[82]:


import requests
import pymongo
import json
from pymongo.errors import BulkWriteError


# ## Api Connection 

# In[41]:


url = "https://unogsng.p.rapidapi.com/genres"

headers = {
    'x-rapidapi-host': "unogsng.p.rapidapi.com",
    'x-rapidapi-key': "c5a36d6e9dmshf9d92e67991693fp18065cjsnbe84f72a4f20"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


# In[48]:


print(type(response1))
response2=json.loads(response1)
print(type(response2))


# In[87]:


response2.popitem()


# In[88]:


response2


# In[107]:


dicti={}
listi=[]
for key,value in response2.items():
    
    dicti["id"]=int(key)
    dicti["name"]=value
    dicti_copy = dicti.copy()

    print(dicti)
    listi.append(dicti_copy)
    
    


# In[108]:


listi


# In[92]:


response3=[{k, response2[k]} for k in response2]


# In[93]:


response3


# ## connection with mongo_db

# In[109]:


client=pymongo.MongoClient("mongodb://127.0.0.1:27017/") #mongodb_client


# In[110]:


mydb=client["Movie1"]


# In[111]:


information=mydb.Movieinformatio


# In[113]:


information.insert_many(listi)
#information.bulk_write(listi)


# In[114]:


## Select * from employeeinformation
for record in information.find({}):
    print(record)


# In[119]:


## Query the json documents based on equality conditions
# Select * from Movie1 where id=7442

for record in information.find({'id':7442}):
    print(record)


# In[120]:


## Query documents using query operators($in,$lt,$gt)
for record in information.find({'name':{'$in':['Actionkrimis','Adventures']}}):
    print(record)


# In[ ]:




