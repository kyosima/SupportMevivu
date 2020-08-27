-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: localhost    Database: support_mevivu
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `passWord` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `status` int DEFAULT '0',
  `createdDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `firstName` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lastName` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `levels` tinyint DEFAULT NULL,
  `avatar` varchar(500) COLLATE utf8_unicode_ci DEFAULT 'Itachi.png',
  `birthDay` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userName_UNIQUE` (`userName`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'mevivu','chinhhung@gmail.com','123',0,'2020-08-17 15:00:06','Nguyễn Chính','Hưng ATM','0335456342',2,'123','2020-08-18'),(4,'admin','btvu2821@gmail.com','pbkdf2:sha256:150000$g3Z2SpDo$08dd7459b2601ed02e8ac70cd334d1ba000408e723198ba37a96c537c9cc6cfc',0,'2020-08-17 15:33:46','Bùi Thế','Vũ','335828494',1,'Itachi.png','2020-02-09'),(5,'admin1','quocminh@gmail.com','pbkdf2:sha256:150000$bA8SLz6K$9f6fc4b752ed6ac9db2d957394f805338c0fe063c72410a8d2b7cf56b6c7b44d',0,'2020-08-17 16:39:28','Nguyễn Quốc','Minh','0972321434',2,'Itachi.png','2020-04-26'),(6,'kyo','kyosima@gmail.com','pbkdf2:sha256:150000$bA8SLz6K$9f6fc4b752ed6ac9db2d957394f805338c0fe063c72410a8d2b7cf56b6c7b44d',0,'2020-08-26 12:03:16','Khách','Hàng','12314141313',3,'Itachi.png','2020-08-12'),(7,'khachhang','an@gmail.com','pbkdf2:sha256:150000$bA8SLz6K$9f6fc4b752ed6ac9db2d957394f805338c0fe063c72410a8d2b7cf56b6c7b44d',0,'2020-08-26 17:18:26','Kyo','khách','1231313142',3,'Itachi.png','2020-08-14');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-27 18:05:03
