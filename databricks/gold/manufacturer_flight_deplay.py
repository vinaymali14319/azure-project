# Databricks notebook source
# MAGIC %run /mount



# COMMAND ----------

flight = spark.read \
     .format('parquet') \
     .option("path",'raw/flight.parquet') \
     .load()

# COMMAND ----------

PLANE = spark.read \
     .format('parquet') \
     .option("path",'raw/PLANE.parquet') \
     .load()

# COMMAND ----------

suv_manufacturer_flight_deplay = flight.join(PLANE, PLANE["tailid"] == flight["TailNum"], "left")


# COMMAND ----------


output_path = '/raw/gold/manufacturer_flight_deplay' 
suv_manufacturer_flight_deplay.write.format('parquet').mode('overwrite').save(output_path)
