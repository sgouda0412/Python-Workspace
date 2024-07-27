from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col
from pyspark.sql.window import Window, WindowSpec



import os

import findspark

findspark.init()
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-17"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
# Initialize a Spark session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Sample data (you can replace this with a path to a text file)
data = ["Hello world", "Hello Spark", "Hello PySpark", "Spark is great"]

# Create an RDD from the sample data
rdd = spark.sparkContext.parallelize(data)

# Convert the RDD to a DataFrame
df = rdd.toDF(["line"])

# Split each line into words
words_df = df.select(explode(split(col("line"), " ")).alias("word"))

# Count the occurrences of each word
word_counts = words_df.groupBy("word").count()

# Show the result
word_counts.show()

# Stop the Spark session
spark.stop()
