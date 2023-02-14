-- lists all records from table second_table where name is present
-- database name will be passed to mysql command
-- results should display score and then name
-- records should be listed by descending order
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
