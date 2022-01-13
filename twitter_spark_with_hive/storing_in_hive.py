import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#create session
spark = SparkSession.builder.master("local[1]") \
                    .appName('readDataFromHdfs') \
                        .enableHiveSupport()\
                    .getOrCreate()

#create dataframe
data_frame = spark.read.csv( "hdfs://localhost:9000//project1/prabhat.csv")
col1=data_frame.columns
#add hedder
df2 = data_frame.select(col(col1[0]).alias("userid"),col(col1[1]).alias("user_name"),col(col1[2]).alias("follower"),col(col1[3]).alias("location"))


df2.show()
dataframe3 = df2.select('userid','user_name','follower')

dataframe3.show()

# Save df to a new table in Hive
dataframe3.createOrReplaceTempView("twitter_table")

# Show the results using SELECT

sqlDF = spark.sql("SELECT * FROM twitter_table")
sqlDF.show()

