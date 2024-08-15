from pyspark.sql import SparkSession
from pyspark import SparkConf
import logging
import sys
import traceback

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

conf = SparkConf().setAppName("PythonWorkerDebug")
conf.set("spark.driver.memory", "8g")
conf.set("spark.executor.memory", "4g")
conf.set("spark.driver.maxResultSize", "8g")
conf.set("spark.python.worker.memory", "8g")
conf.set(
    "spark.executor.extraJavaOptions",
    "-verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps",
)
conf.set("spark.sql.shuffle.partitions", "10")  # Reduce shuffle partitions

spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")


def main():
    try:
        # Start with a smaller dataset
        df = spark.range(0, 1000000, 1, 10)  # 1 million rows, 10 partitions
        logger.info(f"Initial DataFrame created")

        # Try to force some computation and log progress
        df = df.withColumn("value", df["id"] % 100)
        logger.info("Added 'value' column")

        # Perform a simple aggregation
        result = df.groupBy("value").count()
        logger.info("GroupBy operation defined")

        # Force computation with a small action
        logger.info(f"Number of unique values: {result.count()}")

        # If successful, try with more data
        df = spark.range(0, 10000000, 1, 20)  # 10 million rows, 20 partitions
        logger.info(f"Larger DataFrame created")

        df = df.withColumn("value", df["id"] % 1000)
        result = df.groupBy("value").count()
        logger.info(f"Number of unique values in larger dataset: {result.count()}")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        logger.error(traceback.format_exc())
        sys.exit(1)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
