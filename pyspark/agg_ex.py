import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg, max, min

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# create SparkSession
spark = SparkSession.builder.appName("AggregateFunctionsExample").getOrCreate()

# create a sample dataframe
data = [("John", "Hardware", 1000),
        ("Sara", "Software", 2000),
        ("Mike", "Hardware", 3000),
        ("Lisa", "Hardware", 4000),
        ("David", "Software", 5000)]

df = spark.createDataFrame(data, ["name", "category", "sales"])
df.show()

df.select(sum(df.sales).alias("sales_sum")).show()
df.select(count(df.name).alias("count")).show()

df.select(avg(df.sales).alias("sales_avg")).show()
df.select(max(df.sales).alias("sales_max")).show()
df.select(min(df.sales).alias("sales_min")).show()
df.groupBy(df.category).agg(avg(df.sales)).show()
