"""
pyspark data analysis for netflix data
"""

from pyspark.sql import SparkSession

# from pyspark.sql.window import  Window
# from pyspark.sql.functions import row_number, dense_rank, rank, col, when

# Create SparkSession object to interact with Spark functionality.

spark: SparkSession = (
    SparkSession.builder.master("local[*]").appName("Netflix").getOrCreate()
)

netflix_df = (
    spark.read.format("csv")
    .option("inferSchema", "true")
    .option("header", "true")
    .load(
        r"C:\Users\sgouda\Documents\GitHub\Python-Workspace\pyspark\netflix_titles.csv"
    )
)

# Display the total number of rows in the dataframe.
print(f"Total rows: {netflix_df.count()}")

df_filtered = netflix_df.filter(
    (netflix_df.country == "India")
    & (netflix_df.rating == "TV-MA")
    & (netflix_df.type == "Movie")
)
df_filtered.show(3)

netflix_df.createOrReplaceTempView("netflix_data")
result = spark.sql("SELECT * FROM netflix_data")
result.show(5)

query = """ select * from netflix_data where type = 'Movie' """
result_1 = spark.sql(query)
result_1.show(5)
