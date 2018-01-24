from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.setAppName("MyApp")
sc = SparkContext(conf=conf)

# Create an RDD using /user/bigdata/enwiki-10k.csv
lines = sc.textFile("/user/bigdata/enwiki-10k.csv")

# RDD with articles which contain the word computer
cmpcont = lines.filter(lambda x: "computer" in x.lower())

# compute the number of articles (absolute and relative to the total number)
cmpcont.count()                     # absolute (230)
cmpcont.count() / lines.count()     # relative

# Save the articles that contain the word into a file on HDFS
cmpcont.saveAsTextFile("/user/burgemeister/1-spark-computer.txt")

# Compute the number of articles containing the word computer again using only accumulators
counter = sc.accumulator(0)
cmpcont.foreach(lambda x: counter.add(1))
counter.value

# Now use the methods for data frames for computing the number of articles containing the word computer
cmpcont_df = cmpcont.map(lambda x: (x, )).toDF()
cmpcont_df.count()


