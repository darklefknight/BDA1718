students = load '/user/bigdata/10/students' using PigStorage(',') as (name:chararray, id:int);

semesters = load '/user/bigdata/10/semesters' using PigStorage(',') as (id:int, semester:int);