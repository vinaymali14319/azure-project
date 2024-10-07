# Databricks notebook source
# MAGIC %run /mount



# COMMAND ----------

unique_carriers_raw = spark.read \
     .format('csv') \
     .option("header",True) \
     .option("schema", schema) \
     .option("path",'raw/unique_carriers.csv') \
     .load()

# COMMAND ----------

df_unique_carriers = unique_carriers_raw.selectExpr(
    "replace(Code,'\"','') as code",
    "replace(Description,'\"','') as description",
    "to_date(Date_Part,'yyyy-MM-dd') as Date_Part"
)


output_path = '/raw/bronze/unique_carrier' 
df_unique_carriers.write.format('parquet').mode('overwrite').save(output_path)
