-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.16-MariaDB - MariaDB Server
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
  `Lugar_Nacimiento` varchar(255) NOT NULL,
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
  `cohorte` date DEFAULT NULL,
  PRIMARY KEY (`idAlumnos`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.alumnos: ~4 rows (approximately)
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
REPLACE INTO `alumnos` (`idAlumnos`, `Nombre`, `DNI`, `Lugar_Nacimiento`, `Fecha_Nacimiento`, `Edad`, `Domicilio`, `numero`, `piso`, `depto`, `Estado_Civil`, `Localidad`, `Partido`, `CP`, `Telefono`, `Celular`, `Estudios_Cursados`, `Otros`, `Trabaja`, `Ocupacion`, `emergencias`, `osocial`, `Sexo`, `Carrera`, `ciclo`, `horario`, `Nacionalidad`, `hijos`, `acargo`, `mail`, `egreso`, `insti_otros`, `escuela`, `distrito`, `doc_dni`, `doc_Tit`, `doc_Reg`, `doc_fot`, `doc_cert`, `Grupo_Sanguineo`, `Antitetanica`, `Presion_Arterial`, `Enfermedades`, `Tratamiento`, `alergias`, `foto`, `cohorte`) VALUES
	(1, 'Gabriel Garcia', 23235867, '', '0000-00-00', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '0', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 0, NULL, '0', 0, '', '', '0000', ', ', '', '0', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(2, NULL, 23235866, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Tecnicatura', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(3, '', 23235864, '', '0000-00-00', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '0', '', 0, '', '', '', 'Femenino', 'Profesorado de Artes Plásticas', 0, NULL, '0', 0, '', '', '0000', ', ', '', '0', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(4, 'Georgina Comellini', 35330160, 'Avellaneda', '0000-00-00', 26, 'Brandsen', 1692, 'PB', 'A', 'Solterx', 'Crucecita', 'Avellaneda', '1870', 11, 11, 'BAchiller', 'Publicitaria', 1, 'Petróleo', '0800-555-6666', 'OSDE', 'Femenino', 'FOBA', 2016, '9 a 18', 'Avellaneda', 0, '', 'georgina.comellini@gmail.com', '0000', 'ESP, ', 'Zacaría', 'CABA', 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(5, 'tello', 2222222, '', '0000-00-00', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'FOBA', 2016, '', '', 0, '', '', '0000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(6, 'tello', 222556565, '', '2132-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'FOBA', 2016, '', '', 0, '', '', '0000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(7, 'tello2', 221212121, '', '2135-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'FOBA', 2016, '', '', 0, '', '', '0000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(8, 'Octavio', 48803377, '', '2008-01-01', 8, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Masculino', 'FOBA', 2016, '', '', 0, '', '', '0000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(9, 'gastao', 221133445, '', '2152-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'FOBA', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(10, 'gabi', 77777777, '', '2162-01-01', 11, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'FOBA', 2016, '', '', 0, '', '', '2008', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;

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
  PRIMARY KEY (`id_asignatura`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.asignaturas: ~56 rows (approximately)
/*!40000 ALTER TABLE `asignaturas` DISABLE KEYS */;
REPLACE INTO `asignaturas` (`id_asignatura`, `nombre`, `carrera`, `correlativas`, `horario`, `vacantes`, `anio`, `cursada_paralela`) VALUES
	(1, 'DIBUJO', '1', NULL, NULL, NULL, 0, NULL),
	(2, 'PINTURA (TECNOLOGÍA)', '1', NULL, NULL, NULL, 0, NULL),
	(3, 'ESCULTURA CERAMICA (MODELADO)', '1', NULL, NULL, NULL, 0, NULL),
	(4, 'ARTES DEL FUEGO I (DECORACIÓN)', '1', NULL, NULL, NULL, 0, NULL),
	(5, 'ARTES DEL FUEGO II (ALFARERÍA)', '1', NULL, NULL, NULL, 0, NULL),
	(6, 'LENGUAJE VISUAL', '1', NULL, NULL, NULL, 0, NULL),
	(7, 'HISTORIA DEL ARTE Y LA CULTURA', '1', NULL, NULL, NULL, 0, NULL),
	(8, 'INTRODUCCIÓN AL ANÁLISIS', '1', NULL, NULL, NULL, 0, NULL),
	(9, 'DIBUJO I', '5', NULL, NULL, NULL, 1, NULL),
	(10, 'QUÍMICA APLICADA I', '5', NULL, NULL, NULL, 1, NULL),
	(11, 'ALFARERÍA', '2', NULL, NULL, NULL, 1, NULL),
	(12, 'MOLDERÍA I', '2', NULL, NULL, NULL, 1, NULL),
	(13, 'LENGUAJE VISUAL I', '5', NULL, NULL, NULL, 1, NULL),
	(14, 'HISTORIA DEL ARTE I/HISTORIA DE LAS ARTES VISUALES', '5', NULL, NULL, NULL, 1, NULL),
	(15, 'CERÁMICA (MODELADO/DECORACIÓN)', '2', NULL, NULL, NULL, 1, NULL),
	(16, 'PROYECTO Y DISEÑO CERÁMICO I/DIBUJO II', '5', '9,13', NULL, NULL, 2, NULL),
	(17, 'TECNOLOGÍA APLICADA A LA CERÁMICA I', '5', '29,10', NULL, NULL, 2, NULL),
	(18, 'MOLDERÍA II', '2', NULL, NULL, NULL, 2, NULL),
	(19, 'LENGUAJE VISUAL II', '5', '13', NULL, NULL, 2, NULL),
	(20, 'TEORÍA DE LA PERCEPCIÓN Y LA COMUNICACIÓN', '2', NULL, NULL, NULL, 2, NULL),
	(21, 'HISTORIA DEL ARTE II/HISTORIA DE LAS ARTES VISUALES II', '5', '14', NULL, NULL, 2, NULL),
	(22, 'CERÁMICA Y ALFARERÍA(DECORACIÓN/ALFARERÍA/MODELADO) ', '2', NULL, NULL, NULL, 2, NULL),
	(23, 'PROYECTO Y DISEÑO CERÁMICO II/DIBUJO III', '5', '16,19', NULL, NULL, 3, NULL),
	(24, 'TECNOLOGÍA APLICADA A LA CERÁMICA II', '2', NULL, NULL, NULL, 3, NULL),
	(25, 'ARTES, CULTURAS Y ESTÉTICAS EN EL MUNDO CONTEMPORÁNEO (MODELADO)', '2', NULL, NULL, NULL, 3, NULL),
	(26, 'HISTORIA DE LA CERÁMICA Y PROYECTO DE ANÁLISIS', '2', NULL, NULL, NULL, 3, NULL),
	(27, 'ESPACIO INSTITUCIONAL (LENGUAJE VISUAL)', '2', NULL, NULL, NULL, 3, NULL),
	(28, 'CERÁMICA-MOLDERÍA-ALFARERÍA (MODELADO/MATRICERÍA/ALFARERÍA)/CERÁMICA III', '5', '35,17,19,16', NULL, NULL, 3, NULL),
	(29, 'CERÁMICA I (ALFARERÍA/MOLDERÍA/DECORACIÓN)', '3', NULL, NULL, NULL, 1, NULL),
	(30, 'TALLER COMPLEMENTARIO (ESCULTURA/MODELADO)', '3', NULL, NULL, NULL, 1, NULL),
	(31, 'PRÁCTICA DOCENTE I', '3', NULL, NULL, NULL, 1, NULL),
	(32, 'PSICOLOGÍA DE LA EDUCACIÓN I', '3', NULL, NULL, NULL, 1, NULL),
	(33, 'FUNDAMENTOS DE LA EDUCACIÓN', '3', NULL, NULL, NULL, 1, NULL),
	(34, 'HISTORIA SOCIAL GENERAL', '3', NULL, NULL, NULL, 1, NULL),
	(35, 'CERÁMICA II (DECORACIÓN/ALFARERÍA)', '3', '29,10,13,9', NULL, NULL, 2, NULL),
	(36, 'TALLER COMPLEMENTARIO II (ESCULTURA/MODELADO)', '3', '30,9,13', NULL, NULL, 2, NULL),
	(37, 'PRÁCTICA DOCENTE II', '3', '31,33,32', NULL, NULL, 2, NULL),
	(38, 'HISTORIA SOCIOPOLÍTICA DE LATINOAMÉRICA Y ARGENTINA', '3', '34', NULL, NULL, 2, NULL),
	(39, 'DIDÁCTICA GENERAL', '3', '33,32', NULL, NULL, 2, NULL),
	(40, 'PSICOLOGÍA DE LA EDUCACIÓN II', '3', '33,32', NULL, NULL, 2, NULL),
	(41, 'LENGUAJE VISUAL III', '3', '19', NULL, NULL, 3, NULL),
	(42, 'DIDÁCTICA DE LAS ARTES VISUALES I', '3', '39,40,37', NULL, NULL, 3, NULL),
	(43, 'QUÍMICA APLICADA II', '3', '17,35', NULL, NULL, 3, NULL),
	(44, 'MEDIOS AUDIOVISUALES E IMAGEN DIGITAL', '3', '19,16', NULL, NULL, 3, NULL),
	(45, 'HISTORIAS DE LAS ARTES VISUALES III', '3', '21', NULL, NULL, 3, NULL),
	(46, 'PRÁCTICA DOCENTE III', '3', '19,16,35,17,36,21,37,38,39,40', NULL, NULL, 3, 42),
	(47, 'POLÍTICA EDUCATIVA', '3', '39,38', NULL, NULL, 3, NULL),
	(48, 'TEORÍAS DEL ARTE I', '3', '38,21', NULL, NULL, 3, NULL),
	(49, 'CERÁMICA IV', '3', '42,41,23', NULL, NULL, 4, NULL),
	(50, 'DIBUJO IV', '3', '41,23', NULL, NULL, 4, NULL),
	(51, 'ARTES COMBINADAS', '3', '23,16,36', NULL, NULL, 4, NULL),
	(52, 'DIDÁCTICA DE LAS ARTES VISUALES II', '3', '42,47', NULL, NULL, 4, NULL),
	(53, 'PRÁCTICA DOCENTE IV', '3', '41,23,28,43,44,45,42,46,47,48', NULL, NULL, 4, 52),
	(54, 'TEORÍAS DEL ARTE II', '3', '48,45', NULL, NULL, 4, NULL),
	(55, 'METODOLOGÍA DE LA INVESTIGACIÓN', '3', '48,45', NULL, NULL, 4, NULL),
	(56, 'CURSO 1', '4', NULL, NULL, NULL, 99, NULL);
/*!40000 ALTER TABLE `asignaturas` ENABLE KEYS */;

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
  PRIMARY KEY (`id_calif`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.calificaciones: ~24 rows (approximately)
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
REPLACE INTO `calificaciones` (`id_calif`, `id_asign`, `cuatri1`, `cuatri2`, `recup`, `final1`, `final2`, `final3`, `final4`, `nota`, `fecha_final`, `alumno`) VALUES
	(1, 1, 6.3, NULL, NULL, 7, 4, NULL, NULL, 4, '2016-09-27', 23235867),
	(2, 2, 4, NULL, NULL, 8, NULL, NULL, NULL, 4, NULL, 23235867),
	(3, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL, 23235867),
	(4, 4, NULL, NULL, NULL, 4.5, 6, NULL, NULL, 4, NULL, 23235867),
	(5, 5, 0, NULL, NULL, 6.5, NULL, NULL, NULL, 4, NULL, 23235867),
	(6, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL, 23235867),
	(7, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, NULL, 23235867),
	(8, 8, NULL, NULL, 5, NULL, NULL, NULL, NULL, 4, NULL, 23235867),
	(9, 11, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(10, 12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(11, 15, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(12, 18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(13, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235866),
	(14, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235866),
	(15, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235866),
	(16, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235866),
	(17, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235866),
	(18, 9, 4, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(19, 13, 4, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(20, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235866),
	(21, 20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(22, 24, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(23, 27, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(24, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(25, 25, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(26, 16, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867),
	(27, 19, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867);
/*!40000 ALTER TABLE `calificaciones` ENABLE KEYS */;

-- Dumping structure for table imca.carreras
CREATE TABLE IF NOT EXISTS `carreras` (
  `id_carrera` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.carreras: ~5 rows (approximately)
/*!40000 ALTER TABLE `carreras` DISABLE KEYS */;
REPLACE INTO `carreras` (`id_carrera`, `nombre`, `cantidad`) VALUES
	(1, 'FOBA', 8),
	(2, 'TECNICATURA', 20),
	(3, 'PROFESORADO EN ARTES VISUALES', 37),
	(4, 'CURSOS EXTRAPROGRAMATICOS', 1),
	(5, 'AMBAS', 10);
/*!40000 ALTER TABLE `carreras` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
