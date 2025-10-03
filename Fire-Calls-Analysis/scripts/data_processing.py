import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import year, to_date


# SparkSession
spark = SparkSession.builder.master("local").appName("Fire Calls Analysis").getOrCreate()

# DataFrame schema PySpark
schema = StructType([
    StructField("CallNumber", IntegerType(), True),
    StructField("UnitID", StringType(), True),
    StructField("IncidentType", StringType(), True),
    StructField("CallDate", StringType(), True),
    StructField("Address", StringType(), True),
    StructField("City", StringType(), True),
    StructField("Zipcode", StringType(), True),
    StructField("Battalion", StringType(), True),
    StructField("StationArea", StringType(), True),
    StructField("Box", StringType(), True),
    StructField("OriginalPriority", StringType(), True),
    StructField("Priority", IntegerType(), True),
    StructField("FinalPriority", IntegerType(), True),
    StructField("ALSUnit", StringType(), True),
    StructField("CallType", StringType(), True),
    StructField("CallFinalDisposition", StringType(), True),
    StructField("AvailableDtTm", StringType(), True),
    StructField("AddressType", StringType(), True),
    StructField("TacticalBox", StringType(), True),
    StructField("Name", StringType(), True),
    StructField("Delay", DoubleType(), True),
    StructField("Year", IntegerType(), True),  
])


def load_data_pandas(file_path):
    return pd.read_csv(file_path)


def load_data_pyspark(file_path):
    spark = SparkSession.builder.appName("FireCalls").getOrCreate()
    return spark.read.csv(file_path, header=True, inferSchema=True)


def process_data(df):
    df['CallDate'] = pd.to_datetime(df['CallDate'])
    df['Year'] = df['CallDate'].dt.year

    # Handle non-numeric values ​​in priority columns
    df['Priority'] = pd.to_numeric(df['Priority'], errors='coerce') # Convert to numeric, replace invalid values ​​with NaN
    df['FinalPriority'] = pd.to_numeric(df['FinalPriority'], errors='coerce')

    # Treat NaN
    df['Priority'] = df['Priority'].fillna(0).astype(int)  # Replace NaN with 0 and convert to integer
    df['FinalPriority'] = df['FinalPriority'].fillna(0).astype(int)
    
    return df 


def analyze_with_pyspark(spark_df):
    spark_df = spark_df.withColumn("Year", year(to_date("CallDate", "MM/dd/yyyy")))
    counts = spark_df.groupBy("Year").count()
    counts.show()


if __name__ == "__main__":
    file_path = "./data/sf-fire-calls.csv"
    # spark = SparkSession.builder.appName("FireCallsAnalysis").getOrCreate()
    
    df_pandas = load_data_pandas(file_path)
    df_processed = process_data(df_pandas)
    # df_spark = spark.createDataFrame(df_processed, schema)
    
    # analyze_with_pyspark(df_spark)
    # print(df_processed.head())

    print(df_processed.head())


   
