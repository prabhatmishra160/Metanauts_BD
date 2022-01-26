#!/usr/bin/env python
# coding: utf-8

# In[3]:


import boto3
import pandas as pd

s3 = boto3.client('s3')


# In[4]:


s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-2',
    aws_access_key_id='AKIA4S4VHMD7TXRVSB75',
    aws_secret_access_key='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'
)


# In[5]:


# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


# In[7]:


import pandas as pd


# In[8]:


data_frame=pd.read_csv("C:/Users/prabh/Downloads/countries.csv")


# In[9]:


data_frame.head()


# In[11]:


# Upload files to S3 bucket
s3.Bucket('testbucketbro').upload_file(Filename="C:/Users/prabh/Downloads/countries.csv", Key='countries.csv')


# In[12]:


for obj in s3.Bucket('testbucketbro').objects.all():
    print(obj)


# In[13]:


# Load csv file directly into python
obj = s3.Bucket('testbucketbro').Object('countries.csv').get()
df = pd.read_csv(obj['Body'], index_col=0)


# In[14]:


df.head()


# In[20]:


# Download file and read from disc
s3.Bucket('testbucketbro').download_file(Key='countries.csv', Filename='countries.csv')


# In[23]:


df1=pd.read_csv('countries.csv', index_col=0)


# In[24]:


df1.head()


# In[25]:


# Upload files to S3 bucket after update
s3.Bucket('testbucketbro').upload_file(Filename="countries.csv", Key='countries.csv')


# In[ ]:




