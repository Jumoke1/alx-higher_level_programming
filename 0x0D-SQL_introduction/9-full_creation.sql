-- A script that create a table second_table in the database
CREATE TABLE IF NOT EXIST `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, John, 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, Alex, 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, Bob, 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, George, 8);
