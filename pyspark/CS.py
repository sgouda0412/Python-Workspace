from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("Read CSV from URL").getOrCreate()

# URL of the CSV file
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv"

# Read the CSV file from the URL into a DataFrame
df = spark.read.option("header", "true").csv(url)

# Perform some transformations
df_filtered = df.filter(col("age") > 30)
df_selected = df_filtered.select("name", "age", "salary")

# Show the resulting DataFrame
df_selected.show()

# Write the transformed DataFrame back to a new CSV file
df_selected.write.csv("output.csv", header=True)

# Stop the Spark session
spark.stop()
