-- Creating another table with a unique value
CREATE TABLE IF NOT EXISTS hbtn_test_db_5.unique_id (
    id INT(1) NOT NULL UNIQUE,
    name VARCHAR(256)
);
