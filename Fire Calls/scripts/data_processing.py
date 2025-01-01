import pandas as pd
from pyapark.sql import SparkSession


def load_data_pandas(file_path):
    return pd.load_csv(file_path)

def load_data_pyspark(file_path):
    spark = SparkSession.builder.appName("Fire Calls").getOrCreate()
    return spark.read.csv(file_path, header=True, inferSchema=True)

