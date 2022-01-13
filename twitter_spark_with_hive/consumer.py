#This is consumer file

from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
import pandas as pd
import io
from csv import reader


consumer = KafkaConsumer("Covid" , bootstrap_servers=['localhost:9092'])
#storage location
hdfs_path = "hdfs://localhost:9000//project1/prabhat.csv"
#storing message in hdfs
for message in consumer:
    values = message.value.decode("utf-8")
    with hdfs.open(hdfs_path, "at") as f:
        f.write(f"{values}\n")


