-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: mensajeria
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `canales`
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `id_canal` int NOT NULL AUTO_INCREMENT,
  `id_servidor` int DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_canal`),
  KEY `id_servidor` (`id_servidor`),
  CONSTRAINT `canales_ibfk_1` FOREIGN KEY (`id_servidor`) REFERENCES `servidores` (`id_servidor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
INSERT INTO `canales` VALUES (1,1,'Canal1','Canal de Pruebas 1'),(2,1,'Canal2','Canal de Pruebas 2'),(3,2,'Canal3','Canal de Pruebas 3'),(4,2,'Canal4','Canal de Pruebas 4'),(5,3,'Canal5','Canal de Pruebas 5'),(6,3,'Canal6','Canal de Pruebas 6'),(7,4,'Canal7','Canal de Pruebas 7'),(8,5,'Canal8','Canal de Pruebas 8'),(9,5,'Canal9','Canal de Pruebas 9'),(10,6,'Canal10','Canal de Pruebas 10');
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensajes`
--

DROP TABLE IF EXISTS `mensajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensajes` (
  `id_mensaje` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `id_canal` int DEFAULT NULL,
  `contenido` text,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mensaje`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_canal` (`id_canal`),
  CONSTRAINT `mensajes_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `mensajes_ibfk_2` FOREIGN KEY (`id_canal`) REFERENCES `canales` (`id_canal`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensajes`
--

LOCK TABLES `mensajes` WRITE;
/*!40000 ALTER TABLE `mensajes` DISABLE KEYS */;
INSERT INTO `mensajes` VALUES (1,1,1,'Hola a todos','2023-09-29 07:43:04'),(2,2,1,'¡Bienvenidos!','2023-09-29 07:43:04'),(3,3,2,'¿Cómo están?','2023-09-29 07:43:04'),(4,4,2,'Todo bien, gracias','2023-09-29 07:43:04'),(5,5,3,'Probando el canal','2023-09-29 07:43:04'),(6,6,3,'Esto parece genial','2023-09-29 07:43:04'),(7,7,4,'¡Hola mundo!','2023-09-29 07:43:04'),(8,8,5,'Mensaje de prueba','2023-09-29 07:43:04'),(9,9,6,'¡Saludos a todos!','2023-09-29 07:43:04'),(10,10,6,'Aquí estamos','2023-09-29 07:43:04');
/*!40000 ALTER TABLE `mensajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `miembros_servidores`
--

DROP TABLE IF EXISTS `miembros_servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `miembros_servidores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `id_servidor` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_servidor` (`id_servidor`),
  CONSTRAINT `miembros_servidores_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `miembros_servidores_ibfk_2` FOREIGN KEY (`id_servidor`) REFERENCES `servidores` (`id_servidor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `miembros_servidores`
--

LOCK TABLES `miembros_servidores` WRITE;
/*!40000 ALTER TABLE `miembros_servidores` DISABLE KEYS */;
INSERT INTO `miembros_servidores` VALUES (1,1,1),(2,2,1),(3,3,2),(4,4,2),(5,5,3),(6,6,3),(7,7,4),(8,8,5),(9,9,5),(10,10,6);
/*!40000 ALTER TABLE `miembros_servidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servidores`
--

DROP TABLE IF EXISTS `servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidores` (
  `id_servidor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`id_servidor`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidores`
--

LOCK TABLES `servidores` WRITE;
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
INSERT INTO `servidores` VALUES (1,'Servidor1','Servidor de Pruebas 1'),(2,'Servidor2','Servidor de Pruebas 2'),(3,'Servidor3','Servidor de Pruebas 3'),(4,'Servidor4','Servidor de Pruebas 4'),(5,'Servidor5','Servidor de Pruebas 5'),(6,'Servidor6','Servidor de Pruebas 6'),(7,'Servidor7','Servidor de Pruebas 7'),(8,'Servidor8','Servidor de Pruebas 8'),(9,'Servidor9','Servidor de Pruebas 9'),(10,'Servidor10','Servidor de Pruebas 10');
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(255) NOT NULL,
  `contrasenia` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'usuario1','password1','usuario1@example.com'),(2,'usuario2','password2','usuario2@example.com'),(3,'usuario3','password3','usuario3@example.com'),(4,'usuario4','password4','usuario4@example.com'),(5,'usuario5','password5','usuario5@example.com'),(6,'usuario6','password6','usuario6@example.com'),(7,'usuario7','password7','usuario7@example.com'),(8,'usuario8','password8','usuario8@example.com'),(9,'usuario9','password9','usuario9@example.com'),(10,'usuario10','password10','usuario10@example.com');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  6:28:08
