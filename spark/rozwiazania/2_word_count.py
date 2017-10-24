import sys
import pyspark

if __name__ == "__main__":
	sc = pyspark.SparkContext(appName="wordCount")

	lines = sc.textFile(sys.argv[1])
    
	counts = lines.flatMap(lambda x: x.split()) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(lambda l,r: l+r) \
                  .coalesce(1) 
    
	counts.saveAsTextFile(sys.argv[2])
