
-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Company
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

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
-- Table structure for table `DEPARTMENT`
--
DROP DATABASE IF EXISTS `MUSIC`;
CREATE SCHEMA `MUSIC`;
USE `MUSIC`;
DROP TABLE IF EXISTS `ALBUM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ALBUM` (
  `AlbumID` int(9) NOT NULL,
  `Albumname` varchar(10) NOT NULL,
  `Number_of_Tracks` int(9) NOT NULL,
  PRIMARY KEY (`AlbumID`),
  UNIQUE KEY `AlbumID` (`AlbumID`),
  CONSTRAINT `ALBUM_ibfk_1` FOREIGN KEY (`AlbumID`) REFERENCES `TRACK` (`TrackID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;


LOCK TABLES `ALBUM` WRITE;
INSERT INTO `ALBUM` VALUES (1,'Dhruva',2),(2,'Fidaa',3),(3,'Gangleader',1),(4,'Mirchi',2),(5,'Padi_Padi',2);
UNLOCK TABLES;


--
-- Table structure for table `DEPENDENT`
--

DROP TABLE IF EXISTS `PERSON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PERSON` (
  `PersonID` int(9) NOT NULL,
  `Gender` char(1) NOT NULL,
   `Number_of_compositions` int(9) NOT NULL,
  `BirthDay` date DEFAULT NULL,
  `Person_Name` char(10) NOT NULL,
  `Mobile_Number` int(10) NOT NULL,
  PRIMARY KEY (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
LOCK TABLES `PERSON` WRITE;
INSERT INTO `PERSON` VALUES (1,'F',4,'1990-11-01','Devisriprasad',9087654312),(4,'M',4,'1990-10-01','Sid_Sriram',9087655312),(9,'M',3,'1999-12-03','Anurag',9987654312),(2,'M',4,'1991-06-05','Sastry',9987644312),(5,'M',3,'1989-07-04','Anant',9987644912),(8,'M',3,'1980-06-02','Chandrabose',9987644911),(11,'F',4,'1987-11-09','Ramulamma',9987634911),(3,'M',3,'1980-11-12','Thaman',9986744911),(6,'M',3,'1980-11-14','Micky',9988844911),(7,'M',3,'1979-12-14','Keeravani',9988844912),(10,'M',2,'1999-12-16','Vivek',9988844913);
UNLOCK TABLES;

DROP TABLE IF EXISTS `TRACK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TRACK` (
  `TrackID` int(9) NOT NULL,
  `TrackName` char(10) NOT NULL,
  `TrackTime` char(10) NOT NULL,
  `AlbumID` int(9) NOT NULL,
  `Genre` char(10) NOT NULL,
  PRIMARY KEY (`TrackID`),
  #UNIQUE KEY `AlbumID` (`AlbumID`),
  CONSTRAINT `TRACK_ibfk_1` FOREIGN KEY (`AlbumID`) REFERENCES `TRACK` (`TrackID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `TRACK` WRITE;
INSERT INTO `TRACK` VALUES (1,'Choosa','00:04:30',1,'melody'),(2,'Oosupodu','00:03:45',2,'Melody'),(4,'Neethoney','00:03:45',1,'Party'),(5,'Vachinde','00:03:04',2,'Party'),(3,'Hoyna','00:07:45',3,'Melody'),(6,'Barbie_girl','00:03:05',4,'Party'),(9,'Darlingey','00:06:45',4,'Pop'),(8,'Emaipoyaave','00:05:35',5,'Pop'),(10,'Swag_se_Swagat','00:05:05',NULL,'Melody'),(7,'Kallolam','00:06:45',5,'Pop'),(11,'Shape of You','00:10:45',NULL,'Party');
UNLOCK TABLES;


DROP TABLE IF EXISTS `PERSONS_TRACKS`;
CREATE TABLE `PERSONS_TRACKS` (
    `PersonID` int(9) NOT NULL,
    `TrackID` int(9) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;
LOCK TABLES `PERSONS_TRACKS` WRITE;
INSERT INTO `PERSONS_TRACKS` VALUES (1,1),(1,2),(1,3),(1,10),(4,4),(4,5),(4,6),(4,11),(9,7),(9,8),(9,9),(2,1),(2,2),(2,3),(2,4),(5,5),(5,6),(5,7),(8,8),(8,9),(8,10),(11,11),(3,4),(3,5),(3,1),(6,3),(6,8),(6,2),(7,11),(7,6),(7,9),(10,7),(10,10);
UNLOCK TABLES;



/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-12 23:29:32

DROP TABLE IF EXISTS `RELEASE_DATE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RELEASE_DATE` (
  `TrackID` int(9) NOT NULL,
  `R_Date` date DEFAULT NULL,
  `R_time` char(10) NOT NULL,
  PRIMARY KEY (`TrackID`)
 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;


LOCK TABLES `RELEASE_DATE` WRITE;
INSERT INTO `RELEASE_DATE` VALUES (1,'1999-09-12','00:04:30'),(2,'1999-09-12','00:03:32'),(3,'2001-10-15','00:06:45'),(4,'2000-08-26','00:03:34'),(5,'1997-5-23','00:04:32'),(6,'1994-3-21','00:09:32'),(7,'2009-6-10','00:13:32'),(8,'1989-10-6','00:03:12'),(9,'1992-5-6','00:03:12'),(10,'1978-4-3','00:50:32'),(11,'1881-5-15','00:17:32');
UNLOCK TABLES;

DROP TABLE IF EXISTS `FREQUENCY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FREQUENCY` (
  `TrackID` int(9) NOT NULL,
  `Count` int(9) NOT NULL,
  PRIMARY KEY (`TrackID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `FREQUENCY` WRITE;
INSERT INTO `FREQUENCY` VALUES (1,5),(2,1),(3,2),(4,5),(5,12),(6,6),(7,0),(8,9),(9,11),(10,15),(11,100);
UNLOCK TABLES;


CREATE TABLE `LYRICIST` (
  `PersonID` int(9) NOT NULL,
  `Language` char(10) NOT NULL,
  
  PRIMARY KEY (`PersonID`)
  
 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `LYRICIST` WRITE;
INSERT INTO `LYRICIST` VALUES (2,'Telugu'),(5,'Telugu'),(8,'Telugu'),(11,'English');
UNLOCK TABLES;

CREATE TABLE `MUSIC_DIRECTOR` (
  `PersonID` int(9) NOT NULL,
  `Instrument` char(10) NOT NULL,
  
  PRIMARY KEY (`PersonID`)
  
 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `MUSIC_DIRECTOR` WRITE;
INSERT INTO `MUSIC_DIRECTOR` VALUES (6,'Guitar'),(7,'Violin'),(3,'Keyboard'),(10,'Keyboard');
UNLOCK TABLES;

DROP TABLE IF EXISTS `SINGER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SINGER` (
  `PersonID` int(9) NOT NULL,
  `Genre_of_Singer` char(9) NOT NULL,
  PRIMARY KEY (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `SINGER` WRITE;
INSERT INTO `SINGER` VALUES (1,'melody'),(4,'classical'),(9,'pop');
UNLOCK TABLES;
