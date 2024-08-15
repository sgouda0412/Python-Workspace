from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, lit, row_number, rank, dense_rank
import warnings

warnings.filterwarnings("ignore")

spark: SparkSession = SparkSession.builder.master("local[*]").appName("apps").getOrCreate()

df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(
    r"C:\Users\sgouda\Documents\GitHub\Python-Workspace\pyspark\fifa_ds.csv")

df.select("Position", "Team", "Win").show(2)

df.filter(
    ((df.Team == "Uruguay") & (df.Win == 4))
).show()

print(f"Total rows in the dataset: {df.count()}")

# df.createOrReplaceTempView("fifa")
#
# select * from fifa;
df = df.withColumnRenamed("Win", "Winner")

df.show()

df = df.withColumn("Litted", lit("None"))
df.show()
