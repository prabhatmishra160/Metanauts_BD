import pyspark
from pyspark.sql import SparkSession


spark = SparkSession.builder.master("local[1]") \
                    .appName('readDataFromHdfs') \
                        .enableHiveSupport()\
                    .getOrCreate()
data_frame=spark.read.csv("hdfs://localhost:9000/Demo/MOCK_DATA(4).csv",header=True)

data_frame2 = data_frame.withColumn("salary", 
                                  data_frame["salary"]
                                  .cast('int'))
data_frame2.printSchema()
data_frame.printSchema()
data_frame2.show()
data_frame2.describe().show()



#df2=data_frame2.groupby("country").avg().show()

group_data = data_frame2.groupBy("country")
group_data.avg().show()


dataframe3 = data_frame2.select('first_name','last_name')

dataframe3.show()

# Save df to a new table in Hive
dataframe3.createOrReplaceTempView("hive_table")

# Show the results using SELECT

sqlDF = spark.sql("SELECT * FROM hive_table")
sqlDF.show()
