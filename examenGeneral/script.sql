-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Triangulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Triangulo` (
  `idTriangulo` INT NOT NULL AUTO_INCREMENT,
  `area` DECIMAL NOT NULL,
  `perimetro` DECIMAL NOT NULL,
  PRIMARY KEY (`idTriangulo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Circulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Circulo` (
  `idCirculo` INT NOT NULL AUTO_INCREMENT,
  `area` DECIMAL NOT NULL,
  `perimetro` DECIMAL NOT NULL,
  PRIMARY KEY (`idCirculo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Rectangulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Rectangulo` (
  `idRectangulo` INT NOT NULL AUTO_INCREMENT,
  `area` DECIMAL NOT NULL,
  `perimetro` DECIMAL NOT NULL,
  PRIMARY KEY (`idRectangulo`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
