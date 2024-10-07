# Databricks notebook source
# MAGIC %run /mount

# COMMAND ----------

import tabula
import pandas as pd

pdf_path = 'raw/PLANE.pdf'  

dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=False)

df = pd.concat(dfs, ignore_index=True)

spark_df_PLANE = spark.createDataFrame(df)


# COMMAND ----------

df_plane = spark_df_PLANE.selectExpr(
    "tailnum as tailid",
    "type",
    "manufacturer",
    "to_date(issue_date) as issue_date",
    "model",
    "status",
    "aircraft_type",
    "engine_type",
    "cast(year as int) as year",
    "to_date(Date_Part,'yyyy-MM-dd') as Date_Part",
)



output_path = '/raw/bronze/plane' 
df_plane.write.format('parquet').mode('overwrite').save(output_path)
# COMMAND ----------

cancellation_srv = spark.read \
     .format('csv') \
     .option("header",True) \
     .option("schema", schema) \
     .option("path",'raw/Cancellation.csv') \
     .load()
