CREATE DATABASE  IF NOT EXISTS `web_test` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `web_test`;
-- MySQL dump 10.13  Distrib 5.5.16, for osx10.5 (i386)
--
-- Host: localhost    Database: web_test
-- ------------------------------------------------------
-- Server version	5.5.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `wt_user`
--

DROP TABLE IF EXISTS `wt_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wt_user` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_email` varchar(45) NOT NULL,
  `u_username` varchar(45) NOT NULL,
  `u_password` varchar(45) NOT NULL,
  `u_avatar` varchar(45) NOT NULL,
  `u_created_date` datetime NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wt_user`
--

LOCK TABLES `wt_user` WRITE;
/*!40000 ALTER TABLE `wt_user` DISABLE KEYS */;
INSERT INTO `wt_user` VALUES (1,'amyangfei@gmail.com','小秀秀','219755124b9513700d663f375c2d9c6423447396','2c9e977b98313b656cf23dc678d1f710?s=140','2013-04-16 21:02:30'),(2,'yangfei01@hotmail.com','秀秀','39dd3d9deb136aa5721a5db1b3a8185db250963e','82eadeeaaf11b92b684b78d713b64b4f?s=140','2013-04-16 22:04:18');
/*!40000 ALTER TABLE `wt_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-04-16 22:19:07
