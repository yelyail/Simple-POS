/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 10.4.28-MariaDB : Database - donuts
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`donuts` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `donuts`;

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `productName` varchar(100) DEFAULT NULL,
  `price` int(10) DEFAULT NULL,
  `qty` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=812 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `product` */

insert  into `product`(`id`,`productName`,`price`,`qty`) values 
(711,'Alcapone',20,3),
(712,'Strawberry',12,2),
(713,'Classic',10,32),
(714,'Chocomallow',13,2),
(715,'Nutella',15,4),
(716,'Glaze',15,5),
(717,'Snow White',10,40),
(718,'Alcapone',20,3),
(719,'Strawberry',12,2),
(720,'Classic',10,32),
(721,'Sprinkles',15,14),
(722,'Choco Choco',14,2),
(723,'Choco Choco',14,2),
(724,'Snow White',10,2),
(725,'Choco Choco',14,2),
(726,'Snow White',10,2),
(727,'Nutella',15,2),
(728,'Choco Choco',14,2),
(729,'Snow White',10,2),
(730,'Nutella',15,2),
(731,'Glaze',15,2),
(732,'Choco Choco',14,2),
(733,'Snow White',10,2),
(734,'Nutella',15,2),
(735,'Glaze',15,2),
(736,'Alcapone',20,2),
(737,'Choco Choco',14,2),
(738,'Snow White',10,2),
(739,'Nutella',15,2),
(740,'Glaze',15,2),
(741,'Alcapone',20,2),
(742,'Chocomallow',13,2),
(743,'Choco Choco',14,2),
(744,'Snow White',10,2),
(745,'Nutella',15,2),
(746,'Glaze',15,2),
(747,'Alcapone',20,2),
(748,'Chocomallow',13,2),
(749,'Strawberry',12,2),
(750,'Choco Choco',14,2),
(751,'Snow White',10,2),
(752,'Nutella',15,2),
(753,'Glaze',15,2),
(754,'Alcapone',20,2),
(755,'Chocomallow',13,2),
(756,'Strawberry',12,2),
(757,'Classic',10,2),
(758,'Choco Choco',14,2),
(759,'Snow White',10,2),
(760,'Nutella',15,2),
(761,'Glaze',15,2),
(762,'Alcapone',20,2),
(763,'Chocomallow',13,2),
(764,'Strawberry',12,2),
(765,'Classic',10,2),
(766,'Sprinkles',15,2),
(767,'Glaze',15,1),
(768,'Glaze',15,1),
(769,'Nutella',15,2),
(770,'Glaze',15,1),
(771,'Nutella',15,2),
(772,'Alcapone',20,2),
(773,'Glaze',15,1),
(774,'Nutella',15,2),
(775,'Alcapone',20,2),
(776,'Strawberry',12,2),
(777,'Glaze',15,1),
(778,'Nutella',15,2),
(779,'Alcapone',20,2),
(780,'Strawberry',12,2),
(781,'Chocomallow',13,2),
(782,'Glaze',15,1),
(783,'Nutella',15,2),
(784,'Alcapone',20,2),
(785,'Strawberry',12,2),
(786,'Chocomallow',13,2),
(787,'Snow White',10,2),
(788,'Glaze',15,1),
(789,'Nutella',15,2),
(790,'Alcapone',20,2),
(791,'Strawberry',12,2),
(792,'Chocomallow',13,2),
(793,'Snow White',10,2),
(794,'Choco Choco',14,2),
(795,'Glaze',15,1),
(796,'Nutella',15,2),
(797,'Alcapone',20,2),
(798,'Strawberry',12,2),
(799,'Chocomallow',13,2),
(800,'Snow White',10,2),
(801,'Choco Choco',14,2),
(802,'Classic',10,2),
(803,'Glaze',15,1),
(804,'Nutella',15,2),
(805,'Alcapone',20,2),
(806,'Strawberry',12,2),
(807,'Chocomallow',13,2),
(808,'Snow White',10,2),
(809,'Choco Choco',14,2),
(810,'Classic',10,2),
(811,'Sprinkles',15,2);

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `userID` int(10) NOT NULL AUTO_INCREMENT,
  `userName` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `confirmPass` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=23535 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `register` */

insert  into `register`(`userID`,`userName`,`password`,`confirmPass`) values 
(1,'1','1','1'),
(21,'ariel','ariel','ariel');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
