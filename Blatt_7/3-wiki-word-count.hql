FROM wiki SELECT text LIMIT 1
  ROW FORMAT SERDE ’org.apache.hadoop.hive.serde2.RegexSerDe’ with
  SERDEPROPERTIES ("input.regex" = "^([^,]*)$");