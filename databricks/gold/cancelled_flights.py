# Databricks notebook source
# MAGIC %run /mount



# COMMAND ----------

flight = spark.read \
     .format('parquet') \
     .option("path",'raw/flight.parquet') \
     .load()

# COMMAND ----------

Cancellation = spark.read \
     .format('parquet') \
     .option("path",'raw/Cancellation.parquet') \
     .load()

# COMMAND ----------

result_df = Cancellation.join(flight, Cancellation["code"] == flight["CancellationCode"], "inner")

suv_cancelled_flights = result_df.selectExpr(
    "date as date"
    "year(date) as year", 
    "month(date) as month"
     "Description as Description"
)

# COMMAND ----------


output_path = '/raw/gold/cancelled_flights' 
suv_cancelled_flights.write.format('parquet').mode('overwrite').save(output_path)
