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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.alumnos: ~19 rows (approximately)
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
REPLACE INTO `alumnos` (`idAlumnos`, `Nombre`, `DNI`, `Lugar_Nacimiento`, `Fecha_Nacimiento`, `Edad`, `Domicilio`, `numero`, `piso`, `depto`, `Estado_Civil`, `Localidad`, `Partido`, `CP`, `Telefono`, `Celular`, `Estudios_Cursados`, `Otros`, `Trabaja`, `Ocupacion`, `emergencias`, `osocial`, `Sexo`, `Carrera`, `ciclo`, `horario`, `Nacionalidad`, `hijos`, `acargo`, `mail`, `egreso`, `insti_otros`, `escuela`, `distrito`, `doc_dni`, `doc_Tit`, `doc_Reg`, `doc_fot`, `doc_cert`, `Grupo_Sanguineo`, `Antitetanica`, `Presion_Arterial`, `Enfermedades`, `Tratamiento`, `alergias`, `foto`, `cohorte`) VALUES
	(1, 'Gabriel García', 23235867, 'Buenos Aires', '1973-06-18', 48, 'Dorrego', 2279, 'PB', 'A', 'Solterx', 'Sarandí', 'Avellaneda', '1870', 1121950758, 1165831607, 'Perito Mercantil', ', ', 1, 'Petróleo', '0800-555-55555', 'OSPE', 'Masculino', 'Tecnicatura', 2016, '8:30 a 17:30hs', 'Buenos Aires', 0, '', 'ghgarciar@gmail.com', '1994', ', ', 'Escuela Comercial N° 10 "Islas Malvinas"', '1', 1, 1, 1, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2015'),
	(2, 'DIego Espíndola', 30234123, '', '2000-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'FOBA', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(3, 'Gastón Caravallo', 48803376, 'Lanús', '2000-01-01', 21, 'Dorrego', 2279, 'PB', 'B', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Masculino', 'FOBA', 2016, '', 'Lanús', 2, 'No', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(4, 'Gastón Caraballo', 35330160, 'Lanús', '2004-02-08', 21, 'Camino', 1234, '1', 'C', 'Solterx', 'Monte Chingolo', 'Lanús', '1871', 1143216518, 1143211565, 'Comercial', '', 0, '', '', '', 'Masculino', 'Profesorado de Artes Visuales', 2016, '', 'Lanús', 0, 'No', 'gaston.caraballo@gmail.com', '2010', ', ', 'Zaraza', '2', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2015'),
	(5, 'Norma Villalba', 14577551, '', '2000-01-01', 60, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(6, 'Diego Garcia', 1111111, '', '2000-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(7, 'Gabo', 23235866, '', '2000-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(8, 'Héctor Tello', 14254333, '', '2000-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(9, 'Diego', 44444444, '', '2000-01-01', 0, '', 0, '', '', 'Solterx', '', '', '', 0, 0, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(10, '', 123456789, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(11, 'Purito', 132465978, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(12, '', 666666, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(13, 'Putazo', 33333333, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Profesorado de Artes Visuales', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2016'),
	(14, '', 666555444, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(15, '', 555888999, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(16, '', 22113344, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(17, 'pirula', 35353535, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(18, 'pirulito', 23232323, '', '2000-01-01', 0, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Femenino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
	(19, 'Okito', 48803377, '', '2000-01-01', 8, '', NULL, '', '', 'Solterx', '', '', '', NULL, NULL, '', '', 0, '', '', '', 'Masculino', 'Tecnicatura', 2016, '', '', 0, '', '', '2000', ', ', '', '', 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
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
  `duracion` int(11) DEFAULT NULL,
  `valor` double DEFAULT NULL,
  PRIMARY KEY (`id_asignatura`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.asignaturas: ~65 rows (approximately)
/*!40000 ALTER TABLE `asignaturas` DISABLE KEYS */;
REPLACE INTO `asignaturas` (`id_asignatura`, `nombre`, `carrera`, `correlativas`, `horario`, `vacantes`, `anio`, `cursada_paralela`, `duracion`, `valor`) VALUES
	(1, 'DIBUJO', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(2, 'PINTURA (TECNOLOGÍA)', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(3, 'ESCULTURA CERAMICA (MODELADO)', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(4, 'ARTES DEL FUEGO I (DECORACIÓN)', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(5, 'ARTES DEL FUEGO II (ALFARERÍA)', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(6, 'LENGUAJE VISUAL', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(7, 'HISTORIA DEL ARTE Y LA CULTURA', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(8, 'INTRODUCCIÓN AL ANÁLISIS', '1', NULL, NULL, NULL, 0, NULL, NULL, NULL),
	(9, 'DIBUJO I', '5', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(10, 'QUÍMICA APLICADA I', '5', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(11, 'ALFARERÍA', '2', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(12, 'MOLDERÍA I', '2', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(13, 'LENGUAJE VISUAL I', '5', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(14, 'HISTORIA DEL ARTE I/HISTORIA DE LAS ARTES VISUALES', '5', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(15, 'CERÁMICA (MODELADO/DECORACIÓN)', '2', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(16, 'PROYECTO Y DISEÑO CERÁMICO I/DIBUJO II', '5', '9,13', NULL, NULL, 2, NULL, NULL, NULL),
	(17, 'TECNOLOGÍA APLICADA A LA CERÁMICA I', '5', '29,10', NULL, NULL, 2, NULL, NULL, NULL),
	(18, 'MOLDERÍA II', '2', NULL, NULL, NULL, 2, NULL, NULL, NULL),
	(19, 'LENGUAJE VISUAL II', '5', '13', NULL, NULL, 2, NULL, NULL, NULL),
	(20, 'TEORÍA DE LA PERCEPCIÓN Y LA COMUNICACIÓN', '2', NULL, NULL, NULL, 2, NULL, NULL, NULL),
	(21, 'HISTORIA DEL ARTE II/HISTORIA DE LAS ARTES VISUALES II', '5', '14', NULL, NULL, 2, NULL, NULL, NULL),
	(22, 'CERÁMICA Y ALFARERÍA(DECORACIÓN/ALFARERÍA/MODELADO) ', '2', NULL, NULL, NULL, 2, NULL, NULL, NULL),
	(23, 'PROYECTO Y DISEÑO CERÁMICO II/DIBUJO III', '5', '16,19', NULL, NULL, 3, NULL, NULL, NULL),
	(24, 'TECNOLOGÍA APLICADA A LA CERÁMICA II', '2', NULL, NULL, NULL, 3, NULL, NULL, NULL),
	(25, 'ARTES, CULTURAS Y ESTÉTICAS EN EL MUNDO CONTEMPORÁNEO (MODELADO)', '2', NULL, NULL, NULL, 3, NULL, NULL, NULL),
	(26, 'HISTORIA DE LA CERÁMICA Y PROYECTO DE ANÁLISIS', '2', NULL, NULL, NULL, 3, NULL, NULL, NULL),
	(27, 'ESPACIO INSTITUCIONAL (LENGUAJE VISUAL)', '2', NULL, NULL, NULL, 3, NULL, NULL, NULL),
	(28, 'CERÁMICA-MOLDERÍA-ALFARERÍA (MODELADO/MATRICERÍA/ALFARERÍA)/CERÁMICA III', '5', '35,17,19,16', NULL, NULL, 3, NULL, NULL, NULL),
	(29, 'CERÁMICA I (ALFARERÍA/MOLDERÍA/DECORACIÓN)', '3', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(30, 'TALLER COMPLEMENTARIO (ESCULTURA/MODELADO)', '3', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(31, 'PRÁCTICA DOCENTE I', '3', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(32, 'PSICOLOGÍA DE LA EDUCACIÓN I', '3', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(33, 'FUNDAMENTOS DE LA EDUCACIÓN', '3', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(34, 'HISTORIA SOCIAL GENERAL', '3', NULL, NULL, NULL, 1, NULL, NULL, NULL),
	(35, 'CERÁMICA II (DECORACIÓN/ALFARERÍA)', '3', '29,10,13,9', NULL, NULL, 2, NULL, NULL, NULL),
	(36, 'TALLER COMPLEMENTARIO II (ESCULTURA/MODELADO)', '3', '30,9,13', NULL, NULL, 2, NULL, NULL, NULL),
	(37, 'PRÁCTICA DOCENTE II', '3', '31,33,32', NULL, NULL, 2, NULL, NULL, NULL),
	(38, 'HISTORIA SOCIOPOLÍTICA DE LATINOAMÉRICA Y ARGENTINA', '3', '34', NULL, NULL, 2, NULL, NULL, NULL),
	(39, 'DIDÁCTICA GENERAL', '3', '33,32', NULL, NULL, 2, NULL, NULL, NULL),
	(40, 'PSICOLOGÍA DE LA EDUCACIÓN II', '3', '33,32', NULL, NULL, 2, NULL, NULL, NULL),
	(41, 'LENGUAJE VISUAL III', '3', '19', NULL, NULL, 3, NULL, NULL, NULL),
	(42, 'DIDÁCTICA DE LAS ARTES VISUALES I', '3', '39,40,37', NULL, NULL, 3, NULL, NULL, NULL),
	(43, 'QUÍMICA APLICADA II', '3', '17,35', NULL, NULL, 3, NULL, NULL, NULL),
	(44, 'MEDIOS AUDIOVISUALES E IMAGEN DIGITAL', '3', '19,16', NULL, NULL, 3, NULL, NULL, NULL),
	(45, 'HISTORIAS DE LAS ARTES VISUALES III', '3', '21', NULL, NULL, 3, NULL, NULL, NULL),
	(46, 'PRÁCTICA DOCENTE III', '3', '19,16,35,17,36,21,37,38,39,40', NULL, NULL, 3, 42, NULL, NULL),
	(47, 'POLÍTICA EDUCATIVA', '3', '39,38', NULL, NULL, 3, NULL, NULL, NULL),
	(48, 'TEORÍAS DEL ARTE I', '3', '38,21', NULL, NULL, 3, NULL, NULL, NULL),
	(49, 'CERÁMICA IV', '3', '42,41,23', NULL, NULL, 4, NULL, NULL, NULL),
	(50, 'DIBUJO IV', '3', '41,23', NULL, NULL, 4, NULL, NULL, NULL),
	(51, 'ARTES COMBINADAS', '3', '23,16,36', NULL, NULL, 4, NULL, NULL, NULL),
	(52, 'DIDÁCTICA DE LAS ARTES VISUALES II', '3', '42,47', NULL, NULL, 4, NULL, NULL, NULL),
	(53, 'PRÁCTICA DOCENTE IV', '3', '41,23,28,43,44,45,42,46,47,48', NULL, NULL, 4, 52, NULL, NULL),
	(54, 'TEORÍAS DEL ARTE II', '3', '48,45', NULL, NULL, 4, NULL, NULL, NULL),
	(55, 'METODOLOGÍA DE LA INVESTIGACIÓN', '3', '48,45', NULL, NULL, 4, NULL, NULL, NULL),
	(56, 'TRATAMIENTO DE SUPERFICIE', '4', NULL, NULL, NULL, 99, NULL, 4, 100),
	(57, 'ESMALTE SOBRE METALES', '4', NULL, NULL, NULL, 99, NULL, 4, 25),
	(58, 'SERIGRAFÍA', '4', NULL, NULL, NULL, 99, NULL, 4, 400),
	(59, 'VITROFUSIÓN', '4', NULL, NULL, NULL, 99, NULL, 4, 150),
	(60, 'TALLER CERÁMICO', '4', NULL, NULL, NULL, 99, NULL, 4, 150),
	(61, 'REPARACIÓN DE HORNOS', '4', NULL, NULL, NULL, 99, NULL, 4, 300),
	(62, 'MOLDERÍA', '4', NULL, NULL, NULL, 99, NULL, 4, 200),
	(63, 'MODELADO Y MOLDERÍA DIGITAL', '4', NULL, NULL, NULL, 99, NULL, 4, 150),
	(64, 'ALFARERÍA', '4', NULL, NULL, NULL, 99, NULL, 4, 200),
	(65, 'JOYERÍA', '4', NULL, NULL, NULL, 99, NULL, 4, 150);
/*!40000 ALTER TABLE `asignaturas` ENABLE KEYS */;

-- Dumping structure for table imca.caja
CREATE TABLE IF NOT EXISTS `caja` (
  `idMovimiento` int(11) NOT NULL AUTO_INCREMENT,
  `Importe` int(11) NOT NULL DEFAULT '0',
  `Saldo` int(11) NOT NULL DEFAULT '0',
  `Detalle` varchar(255) NOT NULL DEFAULT '0',
  `recibo` int(11) DEFAULT '0',
  PRIMARY KEY (`idMovimiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imca.caja: ~0 rows (approximately)
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.calificaciones: ~12 rows (approximately)
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
REPLACE INTO `calificaciones` (`id_calif`, `id_asign`, `cuatri1`, `cuatri2`, `recup`, `final1`, `final2`, `final3`, `final4`, `nota`, `fecha_final`, `alumno`, `fecha_inscripcion`) VALUES
	(1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5, NULL, 23235867, '2016-10-25'),
	(2, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, 23235867, '2016-10-25'),
	(3, 56, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-30'),
	(4, 57, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-30'),
	(5, 58, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-30'),
	(6, 59, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-30'),
	(7, 60, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-30'),
	(8, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-31'),
	(9, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-31'),
	(10, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 23235867, '2016-10-31'),
	(11, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 35330160, '2016-10-31'),
	(12, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 48803377, '2016-11-01');
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

-- Dumping structure for table imca.cooperadora
CREATE TABLE IF NOT EXISTS `cooperadora` (
  `idMov` int(11) NOT NULL,
  `dni` int(11) NOT NULL COMMENT '= al DNi del Alumno',
  `importe` float NOT NULL,
  `Detalle` varchar(255) NOT NULL,
  PRIMARY KEY (`idMov`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imca.cooperadora: ~0 rows (approximately)
/*!40000 ALTER TABLE `cooperadora` DISABLE KEYS */;
REPLACE INTO `cooperadora` (`idMov`, `dni`, `importe`, `Detalle`) VALUES
	(0, 23235867, 45, 'Zaraza');
/*!40000 ALTER TABLE `cooperadora` ENABLE KEYS */;

-- Dumping structure for table imca.cuentas
CREATE TABLE IF NOT EXISTS `cuentas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `periodo` varchar(50) DEFAULT NULL,
  `asignatura` int(11) NOT NULL DEFAULT '0' COMMENT 'igua ¡l a id de asignatura',
  `importe` double DEFAULT '0',
  `detalle` varchar(255) DEFAULT NULL,
  `dni` int(11) NOT NULL DEFAULT '0',
  `estado` varchar(50) NOT NULL DEFAULT 'Pendiente',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.cuentas: ~38 rows (approximately)
/*!40000 ALTER TABLE `cuentas` DISABLE KEYS */;
REPLACE INTO `cuentas` (`id`, `periodo`, `asignatura`, `importe`, `detalle`, `dni`, `estado`) VALUES
	(1, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(2, 'Octubre 2016', 56, 100, 'CURSO 1', 23235867, 'Pendiente'),
	(3, 'Octubre 2016', 57, 25, 'CURSO II', 23235867, 'Pendiente'),
	(4, 'Octubre 2016', 58, 400, 'CURSO III', 23235867, 'Pendiente'),
	(5, 'Octubre 2016', 59, 150, 'CURSO IV', 23235867, 'Pendiente'),
	(6, 'Octubre 2016', 60, 150, 'CURSO V', 23235867, 'Pendiente'),
	(7, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(8, 'Octubre 2016', 56, 100, 'CURSO 1', 23235867, 'Pendiente'),
	(9, 'Octubre 2016', 57, 25, 'CURSO II', 23235867, 'Pendiente'),
	(10, 'Octubre 2016', 58, 400, 'CURSO III', 23235867, 'Pendiente'),
	(11, 'Octubre 2016', 59, 150, 'CURSO IV', 23235867, 'Pendiente'),
	(12, 'Octubre 2016', 60, 150, 'CURSO V', 23235867, 'Pendiente'),
	(13, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(14, 'Octubre 2016', 56, 100, 'CURSO 1', 23235867, 'Pendiente'),
	(15, 'Octubre 2016', 57, 25, 'CURSO II', 23235867, 'Pendiente'),
	(16, 'Octubre 2016', 58, 400, 'CURSO III', 23235867, 'Pendiente'),
	(17, 'Octubre 2016', 59, 150, 'CURSO IV', 23235867, 'Pendiente'),
	(18, 'Octubre 2016', 60, 150, 'CURSO V', 23235867, 'Pendiente'),
	(19, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(20, 'Octubre 2016', 56, 100, 'CURSO 1', 23235867, 'Pendiente'),
	(21, 'Octubre 2016', 57, 25, 'CURSO II', 23235867, 'Pendiente'),
	(22, 'Octubre 2016', 58, 400, 'CURSO III', 23235867, 'Pendiente'),
	(23, 'Octubre 2016', 59, 150, 'CURSO IV', 23235867, 'Pendiente'),
	(24, 'Octubre 2016', 60, 150, 'CURSO V', 23235867, 'Pendiente'),
	(25, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(26, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(27, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(28, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(29, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(30, 'Octubre 2016', 1, 150, 'Cooperadora', 35330160, 'Pendiente'),
	(31, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(32, 'Octubre 2016', 1, 150, 'Cooperadora', 35330160, 'Pendiente'),
	(33, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(34, 'Octubre 2016', 1, 150, 'Cooperadora', 35330160, 'Pendiente'),
	(35, 'Octubre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(36, 'Octubre 2016', 1, 150, 'Cooperadora', 35330160, 'Pendiente'),
	(37, 'Noviembre 2016', 1, 150, 'Cooperadora', 23235867, 'Pendiente'),
	(38, 'Noviembre 2016', 1, 150, 'Cooperadora', 35330160, 'Pendiente');
/*!40000 ALTER TABLE `cuentas` ENABLE KEYS */;

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

-- Dumping data for table imca.cursos: ~0 rows (approximately)
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;

-- Dumping structure for table imca.recibos
CREATE TABLE IF NOT EXISTS `recibos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `Detalle` varchar(255) DEFAULT NULL,
  `Importe` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table imca.recibos: ~0 rows (approximately)
/*!40000 ALTER TABLE `recibos` DISABLE KEYS */;
/*!40000 ALTER TABLE `recibos` ENABLE KEYS */;

-- Dumping structure for table imca.registros
CREATE TABLE IF NOT EXISTS `registros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.registros: ~39 rows (approximately)
/*!40000 ALTER TABLE `registros` DISABLE KEYS */;
REPLACE INTO `registros` (`id`, `fecha`, `hora`, `user`) VALUES
	(1, '2016-09-30', '17:52:54', 'root'),
	(2, '2016-09-30', '17:53:10', 'root'),
	(3, '2016-09-30', '17:56:29', 'root'),
	(4, '2016-09-30', '17:57:52', 'root'),
	(5, '2016-09-30', '18:01:19', 'root'),
	(6, '2016-09-30', '18:02:08', 'root'),
	(7, '2016-09-30', '18:02:50', 'root'),
	(8, '2016-09-30', '18:03:20', 'root'),
	(9, '2016-09-30', '18:05:38', 'root'),
	(10, '2016-09-30', '18:11:21', 'root'),
	(11, '2016-09-30', '18:13:59', 'root'),
	(12, '2016-09-30', '18:17:01', 'root'),
	(13, '2016-09-30', '18:18:48', 'root'),
	(14, '2016-09-30', '18:21:28', 'root'),
	(15, '2016-09-30', '18:22:24', 'root'),
	(16, '2016-09-30', '10:38:35', 'root'),
	(17, '2016-09-30', '10:44:03', 'root'),
	(18, '2016-09-30', '10:48:08', 'root'),
	(19, '2016-09-30', '10:49:03', 'root'),
	(20, '2016-09-30', '11:10:02', 'root'),
	(21, '2016-09-30', '11:10:30', 'root'),
	(22, '2016-09-30', '11:11:57', 'root'),
	(23, '2016-09-30', '11:54:14', 'root'),
	(24, '2016-09-30', '11:55:41', 'root'),
	(25, '2016-09-30', '11:56:30', 'root'),
	(26, '2016-09-30', '11:57:45', 'root'),
	(27, '2016-09-30', '11:58:14', 'root'),
	(28, '2016-09-30', '11:58:46', 'root'),
	(29, '2016-09-30', '11:59:06', 'root'),
	(30, '2016-09-30', '11:59:24', 'root'),
	(31, '2016-09-30', '13:19:53', 'root'),
	(32, '2016-09-30', '13:21:56', 'root'),
	(33, '2016-09-30', '13:24:33', 'root'),
	(34, '2016-09-30', '14:11:28', 'root'),
	(35, '2016-09-30', '14:12:05', 'root'),
	(36, '2016-09-30', '14:19:58', 'root'),
	(37, '2016-09-30', '14:20:35', 'root'),
	(38, '2016-10-31', '14:21:26', 'root'),
	(39, '2016-11-01', '08:39:01', 'root');
/*!40000 ALTER TABLE `registros` ENABLE KEYS */;

-- Dumping structure for table imca.valores
CREATE TABLE IF NOT EXISTS `valores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) NOT NULL,
  `valor` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Dumping data for table imca.valores: ~3 rows (approximately)
/*!40000 ALTER TABLE `valores` DISABLE KEYS */;
REPLACE INTO `valores` (`id`, `descripcion`, `valor`) VALUES
	(1, 'Cooperadora', 150),
	(2, 'Matricula', 300),
	(3, 'Cursos', 150);
/*!40000 ALTER TABLE `valores` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
