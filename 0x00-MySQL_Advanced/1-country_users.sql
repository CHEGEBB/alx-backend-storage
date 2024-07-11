-- This sql script creates a table users with 
--columns id, email, and name and country
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(255) ENUM('US','CO','TN')
);