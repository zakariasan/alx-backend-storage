-- Write a SQL script that creates a trigger that decreases the quantity
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  UPDATE users
  SET
  average_score = (SELECT AVG(score) FROM corrections where corrections.user_id = user_id)
  where id = user_id
END $$

DELIMITER ;


