# Databricks notebook source
# MAGIC %run /mount

# COMMAND ----------

AIRPORT_srv = spark.read \
     .format('csv') \
     .option("header",True) \
     .option("schema", schema) \
     .option("path",'raw/AIRPORT.csv') \
     .load()

# COMMAND ----------

df_base = AIRPORT_srv.selectExpr(
    "replace(Code,'\"','') as code",
    "replace(Description,'\"','') as description",
    "to_date(Date_Part,'yyyy-MM-dd') as Date_Part"
)

output_path = '/raw/bronze/AIRPORT' 
df.write.format('parquet').mode('overwrite').save(output_path)