from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Data Transformation in PySpark") \
    .getOrCreate()

