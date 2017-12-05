CREATE EXTERNAL TABLE bu_wiki(ID INT, url STRING, title STRING, text STRING)
ROW FORMAT SERDE "org.apache.hadoop.hive.serde2.RegexSerDe" with
SERDEPROPERTIES ("input.regex" = ",([A-Za-z0-9])") LOCATION "/user/bigdata/7/enwiki-clean.csv";