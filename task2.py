#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#import python library
import string
import re


# In[ ]:


path="C:/Users/prabhat/Desktop/task2.txt"   #path of stored file


# In[2]:


#function to read file
                        
def read_file():
    with open(path,"r") as f:
        contents = f.read()
    return preProcessing(contents) #calling data for preprocessing
        
        


# 

# In[3]:


#function to count number of word
def days_count(inputt):
    res=dict()
    split_string=inputt.split()     #split the content after preprocessing
    print("***Total words=",len(split_string))
    for w in set(split_string):
        res[w]=split_string.count(w)
    return res
    


# In[4]:



#Function for Preprocessing
def preProcessing(text):

    text = text.lower()

            
    
    #remove numbers 
    text = text.translate(str.maketrans('', '', string.digits))
    #remove punctauation
    text= text.translate(str.maketrans("","", string.punctuation))
    
    #white space removal
    text = text.strip()
    text = re.sub(r'[^a-zA-z0-9.,!?/:;\"\'\s]', '', text)
    return text


# In[6]:


#Calling function to count number of words


# In[7]:


days_count(read_file())


# In[ ]:





# In[ ]:




