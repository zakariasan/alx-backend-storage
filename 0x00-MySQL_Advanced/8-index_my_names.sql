-- Write a SQL script that creates a table users following these requirements:
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
