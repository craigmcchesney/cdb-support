LOCK TABLES `user_role` WRITE;
SET SESSION FOREIGN_KEY_CHECKS=0;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES
(2,1,1),
(3,1,1),
(4,1,1);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;
