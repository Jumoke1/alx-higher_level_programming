-- Write a script that creates the MySQL server user user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT CONNECT to user_0d_1 IDENTIFIED BY user_0d_1;
GRANT ALL PRIVILEGS
ON *.*
TO 'user_0d_1'@'localhost';

