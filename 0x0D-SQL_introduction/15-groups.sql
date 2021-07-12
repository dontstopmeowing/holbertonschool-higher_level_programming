-- Script that lists the number of records with the same score in the table second_table
-- the number of records for this score will be displayed as a label called number.

SELECT `score`, COUNT(*) as `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;