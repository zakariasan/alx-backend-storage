-- Write a SQL script that creates a table users following these requirements:
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight INT;
    DECLARE avg_weighted_score DECIMAL(10, 2);

    -- Calculate the total weighted score
    SELECT SUM(score * weight) INTO total_score
    FROM students
    JOIN courses ON students.course_id = courses.id;

    -- Calculate the total weight
    SELECT SUM(weight) INTO total_weight
    FROM courses;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update the average weighted score for all students
    UPDATE students
    SET average_weighted_score = avg_weighted_score;
END //

DELIMITER ;

