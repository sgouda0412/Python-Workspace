import os
from pyspark.sql import SparkSession

from pyspark.sql.functions import avg, sum, count

os.environ["PYSPARK_PYTHON"] = (
    r"C:\Users\sgouda\AppData\Local\Programs\Python\Python311\python.exe"
)
os.environ["PYSPARK_DRIVER_PYTHON"] = (
    r"C:\Users\sgouda\AppData\Local\Programs\Python\Python311\python.exe"
)

spark = SparkSession.builder.appName("example").getOrCreate()

# create a DataFrame with a single column "fruit" and several rows
# create a DataFrame with columns "city" and "temperature"
data = [("New York", 10.0), ("New York", 12.0),
        ("Los Angeles", 20.0), ("Los Angeles", 22.0),
        ("San Francisco", 15.0), ("San Francisco", 18.0)]
df = spark.createDataFrame(data, ["city", "temperature"])

df = df.groupBy(df.city).agg(avg(df.temperature).alias("average_temperature"),
                             sum(df.temperature).alias("sum_temperature"),
                             count(df.temperature).alias("count_temperature"))
df.show()
