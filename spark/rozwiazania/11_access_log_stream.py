import pyspark
import pyspark.streaming

# Helper function to read the Apache Access.log data
def get_row(line):
    cols = line.split()
    row = dict()
    source = cols[0]
    method = cols[5].replace('"', '')
    if len(cols) > 8:
        code = cols[8]
    else:
        code = None
    return (source, (method, code))

def get_sets(values):
    d = { 'methods': {v[0] for v in values},
          'codes': {v[1] for v in values}}
    return d

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = pyspark.SparkContext(master="local[2]", appName="AccessLogStreamAnalysis")
ssc = pyspark.streaming.StreamingContext(sc, 10)

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
#grouped.mapValues(lambda values: set(values)).pprint()
grouped.mapValues(get_sets).pprint()

# The stream has to be started explicitly
ssc.start()             
# Wait for strem end
ssc.awaitTermination()