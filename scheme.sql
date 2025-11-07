CREATE DATABASE StudendDB;
USE StudendDB;

CREATE TABLE students (
	id INT auto_increment PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10)
);


SELECT * FROM students;
