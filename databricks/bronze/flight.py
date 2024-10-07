# Databricks notebook source
# MAGIC %run /mount



# COMMAND ----------

flight_raw = spark.read \
     .format('csv') \
     .option("header",True) \
     .option("schema", schema) \
     .option("path",'raw/flight.csv') \
     .load()

# COMMAND ----------

df_flight = flight_raw.selectExpr(
"to_date(concat_ws('-',year,month,dayofmonth),'yyyy-MM-dd') as date",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as deptime",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as CRSDepTime",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as ArrTime",
"from_unixtime(unix_timestamp(case when DepTime=2400 then 0 else DepTime End,'HHmm'),'HH:mm')  as CRSArrTime",
"UniqueCarrier",
"cast(FlightNum as int) as FlightNum",
"cast(TailNum as int) as TailNum" ,
"cast(ActualElapsedTime as int) as ActualElapsedTime",
"cast(CRSElapsedTime as int) as CRSElapsedTime",
"cast(AirTime as int) as AirTime",
"cast(ArrDelay as int) as ArrDelay",
"cast(DepDelay as int) as DepDelay",
 "Origin",
 "Dest",
 "cast(Distance as int) as  Distance",
 "cast(TaxiIn as int) as TaxiIn",
 "cast(TaxiOut as int) as TaxiOut",
 "Cancelled",
 "CancellationCode",
 "cast(Diverted as int) as castDiverted",
 "cast(CarrierDelay as int) as CarrierDelay",
 "cast(WeatherDelay as int) as WeatherDelay" ,
 "cast(NASDelay as int) as NASDelay",
 "cast(SecurityDelay as int) as SecurityDelay",
 "cast(LateAircraftDelay as int) as LateAircraftDelay" ,
 "to_date(Date_Part,'yyyy-MM-dd') as Date_Part "
)


output_path = '/raw/bronze/flight' 
df_flight.write.format('parquet').mode('overwrite').save(output_path)