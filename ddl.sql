-- -----------------------------------------------------
-- Schema payhere
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `payhere` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin ;
USE `payhere` ;

-- -----------------------------------------------------
-- Table `payhere`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `payhere`.`product` (
  `pd_id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `categorie` VARCHAR(45) NOT NULL,
  `price` INT(11) NOT NULL,
  `cost` INT(11) NULL DEFAULT NULL,
  `pd_name` VARCHAR(45) NOT NULL,
  `content` TINYTEXT NULL DEFAULT NULL,
  `barcode` INT(11) NULL DEFAULT NULL,
  `ex_date` DATETIME NOT NULL,
  `size` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`pd_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;

-- -----------------------------------------------------
-- Table `payhere`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `payhere`.`user` (
  `user_id` INT(11) NOT NULL AUTO_INCREMENT,
  `phone_num` VARCHAR(11) NOT NULL,
  `password` CHAR(60) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_bin;
