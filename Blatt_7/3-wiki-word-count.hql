CREATE EXTERNAL TABLE IF NOT EXISTS bu_wiki(text STRING)
LOCATION "/user/7";

SELECT word, count(*) FROM bu_wiki LATERAL
VIEW explode(split(lower(text), '\\W+')) t1 as word
GROUP BY word LIMIT 1000;