-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

drop procedure IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
        DECLARE user_avg FLOAT;
        SELECT AVG(score) INTO user_avg FROM corrections WHERE corrections.user_id=user_id;
        UPDATE users SET average_score=user_avg WHERE id=user_id;
END//

DELIMITER ;