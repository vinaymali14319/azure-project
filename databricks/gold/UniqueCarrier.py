# Databricks notebook source
# MAGIC %run /mount



# COMMAND ----------

flight = spark.read \
     .format('parquet') \
     .option("path",'raw/flight.parquet') \
     .load()

# COMMAND ----------

unique_carrier = spark.read \
     .format('parquet') \
     .option("path",'raw/unique_carrier.parquet') \
     .load()

# COMMAND ----------

suv_unique_carrier = flight.join(unique_carrier, unique_carrier["code"] == flight["UniqueCarrier"], "left")


# COMMAND ----------


output_path = '/raw/gold/unique_carrier' 
suv_unique_carrier.write.format('parquet').mode('overwrite').save(output_path)
