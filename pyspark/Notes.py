# sparksession sparkContext - > entry points to spark cluster to run spark code
# spark 1.8, hiveContext , sqlContext,SparkContext, StreamingContext
# sparksession all are encapsulate

from pyspark.sql import SparkSession

# .master -> which cluster node we want to connect and run code("local[1]")
spark = (
    SparkSession.builder.master("local[1]")
    .appName("testing")
    .config("")
    .getOrCreate()
)

# check .config("")
# spark.newSession
# spark.SparkContext

# what and why Spark, what problem does it solve?
# Ans:-> Spark is a unified computing engine and set of libraries for parallel data \
# processing on computer cluster

# spark doesnot have storage


# Database - > oraclem teradata exadata mysql
# structured format - > tabular format
# After internet - > text csv image videos
# json,yaml , xml -> semi structure

# volume -> 5GB, 10 TB, velocity - > 1 sec, 1 hour, variety -> multi formats data[structured, semi structured, unstructured]


# ETL -> extract transform load
# ELT - > Extract load transform


# issues
# storage
# processing big data [ram, cpu]

# first Haddop enters now SPark

# Monothilic Apporach -> one big system , which handle storage and processing -> increase hardware
# vertical scalling , expensive
# Distributed Apprach  ->
