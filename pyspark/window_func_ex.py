"""
modules
Author:
time:
"""

import os
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, dense_rank, rank, percent_rank
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

import warnings

warnings.filterwarnings("ignore")

os.environ["PYSPARK_PYTHON"] = (
    r"C:\Users\sgouda\AppData\Local\Programs\Python\Python311\python.exe"
)
os.environ["PYSPARK_DRIVER_PYTHON"] = (
    r"C:\Users\sgouda\AppData\Local\Programs\Python\Python311\python.exe"
)

# os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-22"
# os.environ["SPARK_HOME"] = r"C:/spark"
# os.environ["HADOOP_HOME"] = r"C:/hadoop"

# Initialize a SparkSession
spark: SparkSession = (
    SparkSession.builder.master("local[*]")
    .config(
        "spark.eventLog.gcMetrics.youngGenerationGarbageCollectors",
        "G1 Young Generation",
    )
    .config(
        "spark.eventLog.gcMetrics.oldGenerationGarbageCollectors", "G1 Old Generation"
    )
    .appName("SalesDataset")
    .getOrCreate()
)

# Define the schema for the dataset
schema = StructType(
    [
        StructField("date", StringType(), True),
        StructField("item", StringType(), True),
        StructField("sales", IntegerType(), True),
    ]
)

# Create the data
data = [
    ("2022-01", "apple", 100),
    ("2022-01", "banana", 200),
    ("2022-01", "orange", 300),
    ("2022-02", "apple", 150),
    ("2022-02", "banana", 250),
    ("2022-02", "orange", 350),
    ("2022-03", "apple", 200),
    ("2022-03", "banana", 300),
    ("2022-03", "orange", 400),
]

# Create a DataFrame
df = spark.createDataFrame(data, schema)

window = Window.partitionBy("date").orderBy("sales")
df = df.withColumn("row_number", row_number().over(window))

window = Window.partitionBy("date").orderBy("sales")
df = df.withColumn("rank", rank().over(window))

window = Window.partitionBy("date").orderBy("sales")
df = df.withColumn("dense_rank", dense_rank().over(window))

df = df.withColumn("sales_percent_rank", percent_rank().over(window))
df.show()
