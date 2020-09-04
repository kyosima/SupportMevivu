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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `passWord` varchar(500) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `status` int DEFAULT '0',
  `createdDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `firstName` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `lastName` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `levels` tinyint DEFAULT '3',
  `avatar` varchar(500) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT 'Itachi.png',
  PRIMARY KEY (`id`),
  UNIQUE KEY `userName_UNIQUE` (`userName`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'mevivu','chinhhung@gmail.com','123',0,'2020-08-17 15:00:06','Nguyễn Chính','Hưng','01223412332',2,'123'),(4,'admin','btvu2821@gmail.com','pbkdf2:sha256:150000$g3Z2SpDo$08dd7459b2601ed02e8ac70cd334d1ba000408e723198ba37a96c537c9cc6cfc',0,'2020-08-17 15:33:46','Bùi Thế','Vũ','335828494',1,'Itachi.png'),(5,'admin1','quocminh@gmail.com','pbkdf2:sha256:150000$bA8SLz6K$9f6fc4b752ed6ac9db2d957394f805338c0fe063c72410a8d2b7cf56b6c7b44d',0,'2020-08-17 16:39:28','Nguyễn Quốc','Minh','0972321434',2,'Itachi.png'),(6,'kyo','kyosima@gmail.com','pbkdf2:sha256:150000$bA8SLz6K$9f6fc4b752ed6ac9db2d957394f805338c0fe063c72410a8d2b7cf56b6c7b44d',0,'2020-08-26 12:03:16','Selena','Pham','098098098',3,'Itachi.png'),(7,'khachhang','an@gmail.com','pbkdf2:sha256:150000$bA8SLz6K$9f6fc4b752ed6ac9db2d957394f805338c0fe063c72410a8d2b7cf56b6c7b44d',0,'2020-08-26 17:18:26','Kyo','khách','0987557543',3,'Itachi.png'),(8,'dangvy','masad@gmail.com','pbkdf2:sha256:150000$tTLX4UnV$dadf2c136d3086e61010a03b835c9d346261af490e173bc949791b5bbfbe3870',0,'2020-08-28 11:34:36','BÙI','VŨ','1231313131',3,'Itachi.png'),(9,'viethoang','aaaa@gmail.com','pbkdf2:sha256:150000$s4qOa8iZ$3f2d6dad97edb93af84ece6c666e02379c47df38d86dcdf8ec23ac61d61e59c1',0,'2020-08-28 11:41:23','Việt ','Hoàng','0123455678',2,'Itachi.png'),(10,'quocthinh','abc@gmail.com','pbkdf2:sha256:150000$owdGgZ45$079ee2af65876ebd020539073e6f22cdd3ac12dbcd88043833118d6c219e9bb9',0,'2020-08-28 11:45:54','Quốc ','Thịnh','0943452242',2,'Itachi.png'),(11,'quocthinh1','abc@gmail.com','pbkdf2:sha256:150000$UjO5chTR$474279e25b61cc297de7b280b76efe314b30dac5a3b30901384dcc01bb5e2535',0,'2020-08-28 11:47:46','Quốc','Thịnh','0335828494',2,'Itachi.png'),(12,'tronghieu','hieu@gmail.com','pbkdf2:sha256:150000$b8EzGWAu$e7db6ac928b2896305e6107ac0a4559b5a82c880720bf58313cc7a0f5fb8c383',0,'2020-08-28 12:20:28','Trọng','Hiếu','0999999999',2,'Itachi.png'),(13,'david','abc@gmail.com','pbkdf2:sha256:150000$ZXtTnlBG$a77d1c2adbaa9dad4d4d4bf3ff535b5b8d4f65deb91220b3e2dd891721b75748',0,'2020-08-28 14:32:02','Alaba','Davis','09892372931',3,'Itachi.png'),(14,'vanluyen','aaaa@gmail.com','pbkdf2:sha256:150000$YbSBrFI0$2a05f3aecea19b1c8d2e3d96de74ef4d3c627e29ae244601094670211780384e',0,'2020-08-28 14:39:52','Lê Văn','Luyện','0987998832',3,'Itachi.png'),(15,'kythuat','kythuat@gmail.com','pbkdf2:sha256:150000$hfauyrUP$6cfd3fecb40387c490502635032d4bc3ad37addddc89b9ef75e30869cbaa557d',0,'2020-08-28 16:45:34','Nhân viên','Kỹ thuật','345231434',2,'kyo.jpg'),(16,'trangtruong','truong@gmail.com','pbkdf2:sha256:150000$9dXpSnSl$3b2eed507fecfea6201ca3ac0aa5e5b82c94d5ad3c5744d199f7fd33952ed93a',0,'2020-08-31 14:49:39','Trần','Trường','123124213142141',2,'Itachi.png'),(17,'hoangdao','dap@gmail.com','pbkdf2:sha256:150000$ulVhO7Ut$181b8d1fc386253fb690e5964dc8f28f27bcdfaa4be9908d92a63f6e15e4afac',0,'2020-08-31 15:01:44','Hoàng','Đạo','214112313141',2,'Itachi.png'),(18,'trantruong','anv@gmail.com','pbkdf2:sha256:150000$q3AcHiRd$7c5d099b611075e22677735317b71bc4a625c077f412948177e3f94f38814d8f',0,'2020-09-04 15:40:07','Trần','Trương',NULL,3,'Itachi.png');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-04 15:45:17
