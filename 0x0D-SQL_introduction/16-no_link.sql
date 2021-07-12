-- Script that lists all records of the table second_table
-- whilst is NOT NULL or an empty string or tuple listed by descending score.

SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL OR `name` != '' ORDER BY `score` DESC;
