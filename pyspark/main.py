import os
import warnings

from pyspark import SparkConf
from pyspark.sql import SparkSession

warnings.filterwarnings("ignore")

conf = SparkConf().setAppName("PythonWorkerDebug")
conf.set("spark.driver.memory", "16g")  # Reduced memory settings
conf.set("spark.executor.memory", "16g")  # Reduced memory settings
conf.set("spark.driver.maxResultSize", "4g")
conf.set("spark.python.worker.memory", "4g")
conf.set(
    "spark.executor.extraJavaOptions",
    "-verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps",
)
conf.set("spark.sql.shuffle.partitions", "5")

os.environ["PYSPARK_PYTHON"] = (
    r"C:\Users\sgouda\AppData\Local\Programs\Python\Python311\python.exe"
)
os.environ["PYSPARK_DRIVER_PYTHON"] = (
    r"C:\Users\sgouda\AppData\Local\Programs\Python\Python311\python.exe"
)

os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-22"
os.environ["SPARK_HOME"] = r"C:/spark"
os.environ["HADOOP_HOME"] = r"C:/hadoop"

# Check Java installation
java_home = os.getenv("JAVA_HOME")
if java_home is None:
    print("JAVA_HOME environment variable is not set.")
else:
    print(f"JAVA_HOME is set to: {java_home}")

# Check Spark installation
spark_home = os.getenv("SPARK_HOME")
if spark_home is None:
    print("SPARK_HOME environment variable is not set.")
else:
    print(f"SPARK_HOME is set to: {spark_home}")

# Create SparkSession
try:
    spark: SparkSession = (
        SparkSession.builder.master("local[*]").config(conf=conf).getOrCreate()
    )
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    print("SparkSession created successfully!")
except Exception as e:
    print(f"Error creating SparkSession: {e}")

# Create DataFrame
data = [
    ("James", "zen", "Smith", "1991-04-01", "M", 3000),
    ("Michael", "Rose", "zwee", "2000-05-19", "M", 4000),
    ("Robert", "", "Williams", "1978-09-05", "M", 4000),
    ("Maria", "Anne", "Jones", "1967-12-01", "F", 4000),
    ("Jen", "Mary", "Brown", "1980-02-17", "F", 400),
]

columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
try:
    df = spark.createDataFrame(data=data, schema=columns)
    df.show(truncate=False)
except Exception as e:
    print(f"Error Occured: {e}")
