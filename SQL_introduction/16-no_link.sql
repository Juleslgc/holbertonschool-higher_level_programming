-- Script that lists all records of the table second_table of the database hbtn_0c_0.
SELECT score, name FROM second_table
WHERE name != '' OR name IS NOT NULL
ORDER BY score DESC;