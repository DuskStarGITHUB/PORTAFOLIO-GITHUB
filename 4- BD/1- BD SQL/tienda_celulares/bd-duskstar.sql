-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: tienda_de_celulares
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `articulos`
--

DROP TABLE IF EXISTS `articulos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articulos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `descripcion` text,
  `precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articulos`
--

LOCK TABLES `articulos` WRITE;
/*!40000 ALTER TABLE `articulos` DISABLE KEYS */;
INSERT INTO `articulos` VALUES (1,'Protector de Pantalla','Accesorio','Protector de vidrio templado para teléfonos',19.99),(2,'Funda de Cuero','Accesorio','Funda de cuero genuino para teléfonos',39.99),(3,'Protector de Pantalla','Accesorio','Protector de vidrio templado para teléfonos',19.99),(4,'Funda de Cuero','Accesorio','Funda de cuero genuino para teléfonos',39.99),(5,'Protector de Pantalla','Accesorio','Protector de vidrio templado para teléfonos',19.99),(6,'Funda de Cuero','Accesorio','Funda de cuero genuino para teléfonos',39.99),(7,'Protector de Pantalla','Accesorio','Protector de vidrio templado para teléfonos',19.99),(8,'Funda de Cuero','Accesorio','Funda de cuero genuino para teléfonos',39.99);
/*!40000 ALTER TABLE `articulos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_paterno` varchar(45) DEFAULT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `membresia_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `membresia_id` (`membresia_id`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`membresia_id`) REFERENCES `membresias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (3,'Ana','Martínez','Rodríguez','5551234567','ana@example.com','Colonia 789, Villa','1992-03-20',1),(4,'Pedro','Ramírez','Sánchez','5559876543','pedro@example.com','Calle 321, Pueblo','1988-11-05',2),(5,'Ana','Martínez','Rodríguez','5551234567','ana@example.com','Colonia 789, Villa','1992-03-20',1),(6,'Pedro','Ramírez','Sánchez','5559876543','pedro@example.com','Calle 321, Pueblo','1988-11-05',2),(7,'Ana','Martínez','Rodríguez','5551234567','ana@example.com','Colonia 789, Villa','1992-03-20',1),(8,'Pedro','Ramírez','Sánchez','5559876543','pedro@example.com','Calle 321, Pueblo','1988-11-05',2),(9,'Ana','Martínez','Rodríguez','5551234567','ana@example.com','Colonia 789, Villa','1992-03-20',1),(10,'Pedro','Ramírez','Sánchez','5559876543','pedro@example.com','Calle 321, Pueblo','1988-11-05',2);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entradas`
--

DROP TABLE IF EXISTS `entradas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entradas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `producto_id` int DEFAULT NULL,
  `tipo_producto` enum('telefono','articulo') DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_entrada` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `producto_id` (`producto_id`),
  CONSTRAINT `entradas_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `telefonos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `entradas_ibfk_2` FOREIGN KEY (`producto_id`) REFERENCES `articulos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entradas`
--

LOCK TABLES `entradas` WRITE;
/*!40000 ALTER TABLE `entradas` DISABLE KEYS */;
INSERT INTO `entradas` VALUES (41,1,'telefono',5,'2023-08-10'),(42,2,'telefono',3,'2023-08-12'),(43,3,'articulo',10,'2023-08-11'),(44,4,'articulo',7,'2023-08-13'),(45,1,'telefono',5,'2023-08-10'),(46,2,'telefono',3,'2023-08-12'),(47,3,'articulo',10,'2023-08-11'),(48,4,'articulo',7,'2023-08-13');
/*!40000 ALTER TABLE `entradas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membresias`
--

DROP TABLE IF EXISTS `membresias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membresias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_membresia` varchar(50) DEFAULT NULL,
  `estado` enum('activo','inactivo') DEFAULT NULL,
  `beneficios` text,
  `fecha_activacion` date DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membresias`
--

LOCK TABLES `membresias` WRITE;
/*!40000 ALTER TABLE `membresias` DISABLE KEYS */;
INSERT INTO `membresias` VALUES (1,'Premium','activo','Acceso a ofertas exclusivas, soporte prioritario','2023-08-01','2023-12-31'),(2,'Básica','activo','Descuentos estándar en productos seleccionados','2023-08-01','2023-09-30'),(3,'Premium','activo','Acceso a ofertas exclusivas, soporte prioritario','2023-08-01','2023-12-31'),(4,'Básica','activo','Descuentos estándar en productos seleccionados','2023-08-01','2023-09-30'),(5,'Premium','activo','Acceso a ofertas exclusivas, soporte prioritario','2023-08-01','2023-12-31'),(6,'Básica','activo','Descuentos estándar en productos seleccionados','2023-08-01','2023-09-30'),(7,'Premium','activo','Acceso a ofertas exclusivas, soporte prioritario','2023-08-01','2023-12-31'),(8,'Básica','activo','Descuentos estándar en productos seleccionados','2023-08-01','2023-09-30');
/*!40000 ALTER TABLE `membresias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salidas`
--

DROP TABLE IF EXISTS `salidas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salidas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `producto_id` int DEFAULT NULL,
  `tipo_producto` enum('telefono','articulo') DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_salida` date DEFAULT NULL,
  `cliente_id` int DEFAULT NULL,
  `membresia_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `producto_id` (`producto_id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `membresia_id` (`membresia_id`),
  CONSTRAINT `salidas_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `telefonos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `salidas_ibfk_2` FOREIGN KEY (`producto_id`) REFERENCES `articulos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `salidas_ibfk_3` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  CONSTRAINT `salidas_ibfk_4` FOREIGN KEY (`membresia_id`) REFERENCES `membresias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salidas`
--

LOCK TABLES `salidas` WRITE;
/*!40000 ALTER TABLE `salidas` DISABLE KEYS */;
INSERT INTO `salidas` VALUES (37,1,'telefono',1,'2023-08-20',3,1),(38,2,'articulo',1,'2023-08-21',4,2);
/*!40000 ALTER TABLE `salidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sueldos`
--

DROP TABLE IF EXISTS `sueldos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sueldos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_de_sueldo` varchar(25) DEFAULT NULL,
  `cantidad` varchar(25) DEFAULT NULL,
  `trabajador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `trabajador_id` (`trabajador_id`),
  CONSTRAINT `sueldos_ibfk_1` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajadores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sueldos`
--

LOCK TABLES `sueldos` WRITE;
/*!40000 ALTER TABLE `sueldos` DISABLE KEYS */;
INSERT INTO `sueldos` VALUES (1,'Mensual','3000',1),(2,'Semanal','700',2),(3,'Mensual','3000',1),(4,'Semanal','700',2);
/*!40000 ALTER TABLE `sueldos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telefonos`
--

DROP TABLE IF EXISTS `telefonos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telefonos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `sistema_operativo` varchar(50) DEFAULT NULL,
  `memoria_ram` varchar(20) DEFAULT NULL,
  `almacenamiento` varchar(20) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telefonos`
--

LOCK TABLES `telefonos` WRITE;
/*!40000 ALTER TABLE `telefonos` DISABLE KEYS */;
INSERT INTO `telefonos` VALUES (1,'Samsung','Galaxy S21','Android','8 GB','128 GB',999.99),(2,'Apple','iPhone 12','iOS','4 GB','64 GB',899.99),(3,'Samsung','Galaxy S21','Android','8 GB','128 GB',999.99),(4,'Apple','iPhone 12','iOS','4 GB','64 GB',899.99),(5,'Samsung','Galaxy S21','Android','8 GB','128 GB',999.99),(6,'Apple','iPhone 12','iOS','4 GB','64 GB',899.99),(7,'Samsung','Galaxy S21','Android','8 GB','128 GB',999.99),(8,'Apple','iPhone 12','iOS','4 GB','64 GB',899.99);
/*!40000 ALTER TABLE `telefonos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajadores`
--

DROP TABLE IF EXISTS `trabajadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido_paterno` varchar(45) DEFAULT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `feca_nacimiento` date DEFAULT NULL,
  `numero` varchar(45) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajadores`
--

LOCK TABLES `trabajadores` WRITE;
/*!40000 ALTER TABLE `trabajadores` DISABLE KEYS */;
INSERT INTO `trabajadores` VALUES (1,'Juan','García','Pérez','1990-05-15','1234567890','Calle 123, Ciudad','juan@example.com'),(2,'María','López','Gómez','1985-08-22','9876543210','Avenida 456, Pueblo','maria@example.com'),(3,'Juan','García','Pérez','1990-05-15','1234567890','Calle 123, Ciudad','juan@example.com'),(4,'María','López','Gómez','1985-08-22','9876543210','Avenida 456, Pueblo','maria@example.com');
/*!40000 ALTER TABLE `trabajadores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-27 19:55:08
