-- Creating another table with a unique value
CREATE TABLE IF NOT EXISTS hbtn_test_db_5.unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
