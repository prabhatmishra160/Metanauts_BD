
import tweepy


from kafka import KafkaProducer

from json import dumps
import requests
import os
import csv
import time 

from datetime import datetime



import calendar


#twitter authentication setup

API_key="PYlvEC5JMLmaeAbljNgYA2db8"

API_secret="u9vjrFnGU2xuCdAmrtXv5PPs71IvfBVluUvbzo3Sn7M8JKpcKs"


access_token="200766421-Cn8gi37cpBEdgjtM0yhSEnvIgfYdoEzKefM80tIb"


access_token_secret="L0pCXk7b90vCuCNX336RvYAEbxJuWr3QP8UWSsAAa6bvK"



# connected to jump server of twitter
auth=tweepy.OAuthHandler(API_key,API_secret)
# now we can connect from jump server to web server of twitter
auth.set_access_token(access_token,access_token_secret)
# now we can connect to API storge server of twitter
api = tweepy.API(auth)

producer = KafkaProducer(bootstrap_servers="localhost:9092")
#topic_name = "search_ganguly"
#record="userid"+","+"user_name"+","+"follower"+","+"location"
topic_name = "Covid"
def normalize_time(time):
    mytime = datetime.strptime(time, "%y-%m-%d %H:%M:%S.%f%z")
    return (mytime.strftime("%y-%m-%d %H:%M:%S"))
#read Keyword
def get_data_Fromtwitter():
    res= api.search_tweets("COVID-19vaccine OR Booster OR Variant OR outbreak",lang = "en")
   

    record = ""
    
    for i in res:
        
        record += str(i.user.id_str)
        record += ","
        # fetching the full_text attribute
        record += str(i.user.screen_name)
        record += ","


        record += str(i.user.followers_count)
        record += ","
        record += str(i.user.location)
        record+="\n"



    
    
    producer.send(topic_name,str.encode(record))

       
def periodic_call(intervel):
    x=0
    
    while x<=2:
        
        get_data_Fromtwitter()

        time.sleep(intervel)
        x=x+1
periodic_call(60 * 0.1)








    







