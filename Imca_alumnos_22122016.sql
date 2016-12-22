-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.19-MariaDB - MariaDB Server
-- Server OS:                    Linux
-- HeidiSQL Version:             9.3.0.5112
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for imca
CREATE DATABASE IF NOT EXISTS `imca` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `imca`;

-- Dumping structure for table imca.alumnos
CREATE TABLE IF NOT EXISTS `alumnos` (
  `idAlumnos` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `DNI` int(11) NOT NULL,
  `Lugar_Nacimiento` varchar(255) DEFAULT NULL,
  `Fecha_Nacimiento` date DEFAULT NULL,
  `Edad` int(10) unsigned DEFAULT NULL,
  `Domicilio` varchar(255) DEFAULT NULL,
  `numero` int(10) unsigned DEFAULT NULL,
  `piso` varchar(3) DEFAULT NULL,
  `depto` varchar(5) DEFAULT NULL,
  `Estado_Civil` varchar(100) DEFAULT NULL,
  `Localidad` varchar(255) DEFAULT NULL,
  `Partido` varchar(255) DEFAULT NULL,
  `CP` varchar(30) DEFAULT NULL,
  `Telefono` int(10) unsigned DEFAULT NULL,
  `Celular` int(10) unsigned DEFAULT NULL,
  `Estudios_Cursados` varchar(255) DEFAULT NULL,
  `Otros` varchar(255) DEFAULT NULL,
  `Trabaja` tinyint(1) DEFAULT NULL,
  `Ocupacion` varchar(255) DEFAULT NULL,
  `emergencias` varchar(255) DEFAULT NULL,
  `osocial` varchar(255) DEFAULT NULL,
  `Sexo` varchar(100) DEFAULT NULL,
  `Carrera` varchar(255) DEFAULT NULL,
  `ciclo` int(11) DEFAULT NULL,
  `horario` varchar(255) DEFAULT NULL,
  `Nacionalidad` varchar(255) DEFAULT NULL,
  `hijos` tinyint(3) unsigned DEFAULT NULL,
  `acargo` varchar(255) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `egreso` year(4) DEFAULT NULL,
  `insti_otros` text,
  `escuela` varchar(255) DEFAULT NULL,
  `distrito` varchar(50) DEFAULT NULL,
  `doc_dni` tinyint(1) DEFAULT NULL,
  `doc_Tit` tinyint(1) DEFAULT NULL,
  `doc_Reg` tinyint(1) DEFAULT NULL,
  `doc_fot` tinyint(1) DEFAULT NULL,
  `doc_cert` tinyint(1) DEFAULT NULL,
  `Grupo_Sanguineo` varchar(45) DEFAULT NULL,
  `Antitetanica` tinyint(1) DEFAULT NULL,
  `Presion_Arterial` float DEFAULT NULL,
  `Enfermedades` varchar(255) DEFAULT NULL,
  `Tratamiento` tinyint(1) DEFAULT NULL,
  `alergias` varchar(255) DEFAULT NULL,
  `foto` blob,
  `cohorte` year(4) DEFAULT NULL,
  PRIMARY KEY (`idAlumnos`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
