from pyspark import SparkConf, SparkContext
import re
import collections

# Call spark using this for example:
# PYSPARK_PYTHON=python3 pyspark --master yarn-client --driver-memory 500m --executor-memory 500m --conf spark.ui.port=4711



def parseInput(sc,file_name="/user/bigdata/enwiki-10k.csv"):
    # Read in the data and clean it
    rdd = sc.textFile(file_name)
    return rdd



if __name__ == "__main__":
    conf = SparkConf()
    conf.setAppName("Distance")
    sc = SparkContext(conf=conf)
    articles = parseInput(sc)

    # counter = sc.accumulator(0)
    # numerated_articles = articles.map(lambda x: (x,counter.add(1)))
    words_in_article = articles.map(lambda x: (x.split(" ")))



