CREATE EXTERNAL TABLE IF NOT EXISTS bu_wiki(text STRING)
LOCATION "/user/bigdata/7/enwiki-clean.csv";

SELECT word, count(*) FROM bu_wiki
LATERAL VIEW explode(split(lower(text), '\\W+'))  t1 AS word
GROUP BY word;