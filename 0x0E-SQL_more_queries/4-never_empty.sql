--  creates the table id_not_null on your MySQL server.
-- create table where id must be there

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)

	);
