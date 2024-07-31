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
#df.createDataframe(data, schema = schema)
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


# Hadoop Vs Spark Misconception
# Hadoop is a Database, Spark is 100 times faster than hadoop, Spark process data on Ram/Memory but Hadoop dont
# Hadoop Vs Spark -> difference
# slower, write and read data from disk to in memory | do all the computation in memory
# Hadoop works on Map reduce Paradigm
# Hadoop -> batch processing | Spark -> batch and streaming Processing
# difficult to write code in Hadoop | easy to wite [low + high level API]
# kerberous authentication | doesn't have a solid security feautures[HDFS - ACL, YARN - Kerberos]
#  fault tolerant | fault tolerant


# spark ecosystem
# run on above spark core -> DF, Spark SQL [DF, Dataset]
# spark writtern in Scala -> RDD
# doesnot have cluster manager [ Name ] [YARM, Mesos, Kubernetes, Standalone]
#

#df.createOrReplaceTempView("my_table")

#spark architecture
# cluster -> multiple computer connected through networks
# works based on master slave architecture
# yarn is installed in master -> also called as resources manager
# Node manager - > worker nodes

# spark submit-> spark code goes to resources manager, config-> driver , executer, no of executor , cpu core
# yet another resources nagotiator
# Application master

#transformation and Actions
# Tranformation :-> Anything done on data for processing [Eg:-> select, filter, join , groupby]
# Actions :-> .show(), .count(),.collect(), run one after one 
# lazy evaluation only work after calling actions

# type of transformation
# Narrow :  doesn't require data movement between partitions eg: filter select union map
# wide : avoid it , because data shuffling happens
# wide : groupby, expensive task data shuffling , join, distinct, etc




