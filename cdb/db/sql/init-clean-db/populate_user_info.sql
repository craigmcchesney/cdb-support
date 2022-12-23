LOCK TABLES `user_info` WRITE;
SET SESSION FOREIGN_KEY_CHECKS=0;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES
(1,'cdb','CDB','System Account',NULL,NULL,NULL,''),
(2,'cmcchesney','Craig','McChesney',NULL,NULL,NULL,NULL),
(3,'mdalesio','Michael','Dalesio',NULL,NULL,NULL,NULL),
(4,'jricks','Joseph','Ricks',NULL,NULL,NULL,NULL),
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
