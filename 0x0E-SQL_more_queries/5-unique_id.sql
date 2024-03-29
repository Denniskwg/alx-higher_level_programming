-- creates the table unique_id on your MySQL server
-- database name will be passed as an argument of the mysql command
-- If the table unique_id already exists, your script should not fail
-- id should have a default value of 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
