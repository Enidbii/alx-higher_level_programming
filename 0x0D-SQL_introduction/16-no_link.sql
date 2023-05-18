-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
--SELECT .. FROM .. WHERE .. ORDER BY

SELECT score, name FROM second_table WHERE name IS NOT NUL AND name != '' ORDER BY score DESC;
