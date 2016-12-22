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
-- Dumping structure for table imca.asignaturas
CREATE TABLE IF NOT EXISTS `asignaturas` (
  `id_asignatura` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `carrera` varchar(255) NOT NULL,
  `correlativas` text COMMENT 'igual a id_asignaturas',
  `horario` text,
  `vacantes` text,
  `anio` tinyint(4) DEFAULT NULL,
  `cursada_paralela` int(11) DEFAULT NULL COMMENT 'igual a id_asignatura',
  `duracion` int(11) DEFAULT NULL,
  `valor` double DEFAULT NULL,
  PRIMARY KEY (`id_asignatura`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.caja
CREATE TABLE IF NOT EXISTS `caja` (
  `idMovimiento` int(11) NOT NULL AUTO_INCREMENT,
  `Importe` int(11) NOT NULL DEFAULT '0',
  `Saldo` int(11) NOT NULL DEFAULT '0',
  `Detalle` text NOT NULL,
  `recibo` int(11) DEFAULT '0',
  `fecha` date DEFAULT NULL,
  `tipo` tinyint(4) DEFAULT NULL,
  `doc` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idMovimiento`)
) ENGINE=InnoDB AUTO_INCREMENT=326 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.calificaciones
CREATE TABLE IF NOT EXISTS `calificaciones` (
  `id_calif` int(11) NOT NULL AUTO_INCREMENT,
  `id_asign` int(11) NOT NULL,
  `cuatri1` float DEFAULT NULL,
  `cuatri2` float DEFAULT NULL,
  `recup` float DEFAULT NULL,
  `final1` float DEFAULT NULL,
  `final2` float DEFAULT NULL,
  `final3` float DEFAULT NULL,
  `final4` float DEFAULT NULL,
  `nota` float DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `alumno` bigint(20) NOT NULL COMMENT 'Igual a dni_alumnos',
  `fecha_inscripcion` date DEFAULT NULL,
  PRIMARY KEY (`id_calif`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.carreras
CREATE TABLE IF NOT EXISTS `carreras` (
  `id_carrera` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.cooperadora
CREATE TABLE IF NOT EXISTS `cooperadora` (
  `idMov` int(11) NOT NULL AUTO_INCREMENT,
  `dni` int(11) NOT NULL COMMENT '= al DNi del Alumno',
  `importe` float NOT NULL,
  `Detalle` varchar(255) NOT NULL,
  `anio` year(4) NOT NULL,
  PRIMARY KEY (`idMov`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.cuentas
CREATE TABLE IF NOT EXISTS `cuentas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Alumno` varchar(255) NOT NULL,
  `dni` int(11) NOT NULL DEFAULT '0',
  `periodo` varchar(50) DEFAULT NULL,
  `asignatura` int(11) NOT NULL DEFAULT '0' COMMENT 'igua ¡l a id de asignatura',
  `importe` double DEFAULT '0',
  `detalle` varchar(255) DEFAULT NULL,
  `estado` varchar(50) NOT NULL DEFAULT 'Pendiente',
  `docente` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.cursos
CREATE TABLE IF NOT EXISTS `cursos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` bigint(20) DEFAULT NULL,
  `curso` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `meses` int(11) DEFAULT NULL,
  `costo` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.recibos
CREATE TABLE IF NOT EXISTS `recibos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `Detalle` text,
  `Importe` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `Domicilio` varchar(255) DEFAULT NULL,
  `DNI` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=403 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.registros
CREATE TABLE IF NOT EXISTS `registros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
-- Dumping structure for table imca.valores
CREATE TABLE IF NOT EXISTS `valores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) NOT NULL,
  `valor` double NOT NULL,
  `anual` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
