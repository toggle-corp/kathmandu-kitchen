CREATE TABLE IF NOT EXISTS user ( `id` INT(11) NOT NULL AUTO_INCREMENT, `username` VARCHAR(30) NOT NULL, `password` VARCHAR(255) NOT NULL, PRIMARY KEY (`id`), UNIQUE KEY `username` (`username`))