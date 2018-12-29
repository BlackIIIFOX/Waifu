-- MySQL dump 10.13  Distrib 5.7.20, for Win64 (x86_64)
--
-- Host: localhost    Database: waifu
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `answer_const`
--

DROP TABLE IF EXISTS `answer_const`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer_const` (
  `Id_answer` int(11) NOT NULL AUTO_INCREMENT,
  `Id_const` int(11) NOT NULL,
  `Text_answer` char(100) NOT NULL,
  PRIMARY KEY (`Id_answer`),
  KEY `FK_answer_const` (`Id_const`),
  CONSTRAINT `FK_answer_const` FOREIGN KEY (`Id_const`) REFERENCES `lang_const` (`Id_const`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_const`
--

LOCK TABLES `answer_const` WRITE;
/*!40000 ALTER TABLE `answer_const` DISABLE KEYS */;
INSERT INTO `answer_const` VALUES (1,1,'И тебе привет.'),(2,1,'Здравствуй,семпай.'),(3,1,'Хай.'),(4,1,'И тебе привет.'),(5,1,'Привет.'),(6,2,'Я все еще 2D,так что отлично.');
/*!40000 ALTER TABLE `answer_const` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lang_const`
--

DROP TABLE IF EXISTS `lang_const`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lang_const` (
  `Id_const` int(11) NOT NULL AUTO_INCREMENT,
  `Name_const` char(30) NOT NULL,
  PRIMARY KEY (`Id_const`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lang_const`
--

LOCK TABLES `lang_const` WRITE;
/*!40000 ALTER TABLE `lang_const` DISABLE KEYS */;
INSERT INTO `lang_const` VALUES (1,'Приветствие'),(2,'Состояние');
/*!40000 ALTER TABLE `lang_const` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `text_const`
--

DROP TABLE IF EXISTS `text_const`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `text_const` (
  `Id_text` int(11) NOT NULL AUTO_INCREMENT,
  `Id_const` int(11) NOT NULL,
  `Text_const` char(100) NOT NULL,
  PRIMARY KEY (`Id_text`),
  KEY `FK_text_const` (`Id_const`),
  CONSTRAINT `FK_text_const` FOREIGN KEY (`Id_const`) REFERENCES `lang_const` (`Id_const`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `text_const`
--

LOCK TABLES `text_const` WRITE;
/*!40000 ALTER TABLE `text_const` DISABLE KEYS */;
INSERT INTO `text_const` VALUES (1,1,'Привет.'),(2,1,'Здорово.'),(3,1,'Приветствую.'),(4,1,'Привет!'),(5,1,'Привет.'),(6,1,'Привет.'),(7,1,'Привет машина!'),(8,1,'И тебе привет!'),(9,1,'Здравствуй!'),(10,1,'Здравствуй штука!'),(11,1,'Здравствуйте'),(12,1,'Здорово'),(13,1,'Здорово'),(14,1,'Здравствуйте'),(15,1,'Здорово'),(16,1,'приветствую вас'),(17,1,'приветствую вас'),(18,1,'приветствую тебя'),(19,1,'хай,'),(20,1,'хай!'),(21,1,'hi'),(22,1,'hi'),(23,1,'hello'),(24,2,'Как дела?'),(25,2,'Как дела'),(26,2,'Как твои дела?'),(27,2,'Как самочувствие?'),(28,2,'Как твое самочувствие?'),(29,2,'Что делаешь?'),(30,2,'Что сейчас делаешь?'),(31,2,'Чем занята?'),(32,2,'Чем занята сейчас?'),(33,2,'Как самочувствие у тебя?'),(34,2,'Что нового?'),(35,2,'Что нового у тебя?'),(36,2,'Как жизнь?'),(37,2,'Как поживаешь?'),(38,2,'Как жизуха?'),(39,2,'Как твоя жизнь?');
/*!40000 ALTER TABLE `text_const` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-24 16:40:01
