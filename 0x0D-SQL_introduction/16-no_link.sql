-- lists the number of records with the same score in the table second_table
-- result should display score and number of records for this score
-- list should be sorted by the number of records (descending)
-- database name will be passed as an argument to the mysql command
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
