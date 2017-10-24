import pyspark

import pyspark.sql.functions as func



spark = pyspark.sql.SparkSession.builder \
    .appName('structure_streaming') \
    .master('local[2]') \
    .getOrCreate()

spark.sparkContext.setLogLevel('WARN')    
    
log = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 8899) \
    .load()

out = log \
    .writeStream \
    .trigger(processingTime='5 seconds') \
    .outputMode("append") \
    .format("console") \
    .start()

out.awaitTermination()
