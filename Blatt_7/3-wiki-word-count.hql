FROM wiki SELECT text
  ROW FORMAT SERDE ’org.apache.hadoop.hive.serde2.RegexSerDe’ with
  SERDEPROPERTIES ("input.regex" = "^([^,]*)$");