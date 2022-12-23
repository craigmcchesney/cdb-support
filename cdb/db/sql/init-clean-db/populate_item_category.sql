LOCK TABLES `item_category` WRITE;
SET SESSION FOREIGN_KEY_CHECKS=0;
/*!40000 ALTER TABLE `item_category` DISABLE KEYS */;
INSERT INTO `item_category` VALUES
(1,'Vacuum','',2),
(2,'Diagnostics','',2),
(3,'Controls/Instrumentation',NULL,2),
(5,'Power Systems','',2),
(6,'Magnets',NULL,2),
(7,'RF',NULL,2),
(8,'Beamlines','',2),
(9,'Insertion Devices','',2),
(10,'Lattice Elements',NULL,2),
(12,'Safety Interlocks','',2),
(13,'Generic Functions/Placeholders','',2),
(15,'Supports','',2),
(17,'Front Ends','Components used in front ends',2),
(19,'Test Stands','',2),
(20,'IT','Information Technology',2),
(21,'Survey/Alignment','',2),
(22,'Experimental Facilities Ops','',2),
(23,'Vacuum','',7),
(24,'Diagnostics',NULL,7),
(25,'Controls/Instrumentation',NULL,7),
(26,'Power Systems','',7),
(27,'Magnets',NULL,7),
(28,'RF',NULL,7),
(29,'Mechanical/Beamlines',NULL,7),
(30,'Insertion Devices','',7),
(31,'Lattice Elements',NULL,7),
(32,'Safety Interlocks','',7),
(33,'Generic Functions/Placeholders','',7),
(34,'Supports','',7),
(35,'Front Ends','Components used in front ends',7),
(36,'Test Stands','',7),
(37,'IT','Information Technology',7),
(38,'Survey/Alignment','',7),
(39,'Experimental Facilities Ops','',7),
(41,'Vacuum','',9),
(42,'Diagnostics',NULL,9),
(43,'Controls/Instrumentation',NULL,9),
(44,'Power Systems','',9),
(45,'Magnets',NULL,9),
(46,'RF',NULL,9),
(47,'Mechanical/Beamlines',NULL,9),
(48,'Insertion Devices','',9),
(49,'Lattice Elements',NULL,9),
(50,'Safety Interlocks','',9),
(51,'Generic Functions/Placeholders','',9),
(52,'Supports','',9),
(53,'Front Ends','Components used in front ends',9),
(54,'Test Stands','',9),
(55,'IT','Information Technology',9),
(56,'Survey/Alignment','',9),
(57,'Experimental Facilities Ops','',9),
(59,'Radiation Safety','Components that are used to provide radiation safety',2),
(62,'Water','Accelerator Water Systems',2);
/*!40000 ALTER TABLE `item_category` ENABLE KEYS */;
UNLOCK TABLES;