-- Write a SQL script that creates a trigger that decreases the quantity
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;

