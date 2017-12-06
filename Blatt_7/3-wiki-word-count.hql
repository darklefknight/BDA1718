CREATE EXTERNAL TABLE IF NOT EXISTS bu_wiki(text STRING)
LOCATION "/user/bigdata/7/enwiki-clean.csv";


INSERT overwrite local directory '/home/gux/output7/bu_wiki_out.csv' row format delimited fields terminated by ";"
SELECT text,row_number() over() word, count(*) FROM bu_wiki
LATERAL VIEW explode(split(lower(text), '\\W+'))  t1 AS word
GROUP BY word,row;