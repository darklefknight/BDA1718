DROP TABLE bu_wiki;
CREATE EXTERNAL TABLE bu_wiki(text STRING)
LOCATION "/user/gux/7";

SELECT word, count(*) FROM bu_wiki LATERAL
VIEW explode(split(lower(text), '\\w+')) t1 as word
GROUP BY word LIMIT 1000;