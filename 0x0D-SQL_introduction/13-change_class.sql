-- Script that removes all records with a score <= 5 in the table second_table from a specific database.

DELETE FROM `second_table` WHERE `score` <= 5;
