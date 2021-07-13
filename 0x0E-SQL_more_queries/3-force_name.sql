-- Script that creates a table called force_name in a specific database.

CREATE TABLE
IF
	NOT EXISTS `force_name` ( `id` INT, `name` VARCHAR ( 256 )  NOT NULL );
