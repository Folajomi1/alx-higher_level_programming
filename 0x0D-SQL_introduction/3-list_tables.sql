-- Script that lists all the tables of a database in MySQL server
SELECT table_name -- Select the table_name column from the information_schema.tables table
FROM information_schema.tables -- Get all tables from the information_schema database
WHERE table_schema = DATABASE() -- Filter by the current database
ORDER BY table_name; -- Sort the table names alphabetically

-- End of script
