-- Script that creates a table called first_table in the current database.
USE mysql;
CREATE TABLE if NOT EXISTS first_table(
    id INT, 
    name VARCHAR(256)
    );