-- Write a SQL script that creates a table users following these requirements:
CREATE INDEX idx_name_first_score ON names (name(1), score);
