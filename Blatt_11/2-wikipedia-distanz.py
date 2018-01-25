from pyspark import SparkConf, SparkContext
from operator import add
import re
from collections import Counter

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

    # count words per article
    nwords_article = articles.map(lambda line: Counter(line.split(' ')))



    print((nwords_article.take(4)[0]+nwords_article.take(4)[1]))
    print("TEST")



