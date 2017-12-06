CREATE EXTERNAL TABLE IF NOT EXISTS bu_wiki(text STRING)
LOCATION "/user/bigdata/7/enwiki-clean.csv";

SELECT word, count(*) FROM bu_wiki LATERAL
VIEW explode(split(lower(text), '\\w+')) t1 as word
GROUP BY word LIMIT 1000;