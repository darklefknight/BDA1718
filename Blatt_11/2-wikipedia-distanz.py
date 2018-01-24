from pyspark import SparkConf, SparkContext
import re
import collections

# Call spark using this for example:
# PYSPARK_PYTHON=python3 pyspark --master yarn-client --driver-memory 500m --executor-memory 500m --conf spark.ui.port=4711

conf = SparkConf()
conf.setAppName("MyApp")
sc = SparkContext(conf=conf)

def parseInput(file_name="/user/bigdata/wikipedia-text-tiny-clean500"):
    # Read in the data and clean it
    rdd = sc.textFile(file_name)
    return rdd



rdd = parseInput()
# Print the first 10 lines.
print(rdd.take(10))
