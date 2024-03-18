-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user and set passwd
CREATE USER OF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- hbnb_test should have all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGE ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- grant select privilege on performance_schema to hbnb_test
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
