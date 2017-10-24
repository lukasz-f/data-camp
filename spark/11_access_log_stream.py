import pyspark
import pyspark.streaming

# Helper function to read the Apache Access.log data
def get_row(line):
    cols = line.split()
    row = dict()
    source = cols[0]
    method = cols[5]
    return (source, method)

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = pyspark.SparkContext(master="local[2]", appName="AccessLogStreamAnalysis")
ssc = pyspark.streaming.StreamingContext(sc, 1)

# Decrease logging level
logger = sc._jvm.org.apache.log4j
logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

# We read from text socket on port 8899
lines = ssc.socketTextStream("localhost", 8899)

# Extract rows
rows = lines.map(lambda l: get_row(l))

# Count the number of rows
count = rows.count()
count.pprint()

# Get all the methods used
grouped = rows.groupByKey()
grouped.mapValues(lambda values: set(values)).pprint()

# The stream has to be started explicitly
ssc.start()             
# Wait for strem end
ssc.awaitTermination()