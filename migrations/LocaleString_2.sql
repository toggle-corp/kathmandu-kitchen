ALTER TABLE `locale_string` MODIFY `locales` INT(11);
ALTER TABLE `locale_string` ADD FOREIGN KEY (`locales`) REFERENCES `locales`(`id`) ON DELETE CASCADE;