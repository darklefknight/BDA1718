num = load '/user/bigdata/10/numbers' as number:int

grouped   = group num all;

avg       = foreach grouped generate AVG(num.number);