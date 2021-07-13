-- script that creates the database hbtn_0d_usa and a the chill table cities
-- that's linked with the table states using a foreing key.

CREATE DATABASE
IF
	NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE
IF
	NOT EXISTS `cities` (
		`id` INT NOT NULL UNIQUE AUTO_INCREMENT,
		`state_id` INT NOT NULL,
		`name` VARCHAR ( 256 ) NOT NULL,
	PRIMARY KEY ( `id` ),
	FOREIGN KEY ( `state_id` ) REFERENCES states ( `id` ));
