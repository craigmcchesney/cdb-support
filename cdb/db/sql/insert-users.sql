LOCK TABLES `user_info` WRITE;
SET SESSION FOREIGN_KEY_CHECKS=0;
INSERT INTO `user_info` (id, username, first_name, last_name, password) VALUES
(2,'cmcchesney','Craig','McChesney',NULL),
(3,'mdalesio','Michael','Dalesio',NULL),
(4,'jricks','Joseph','Ricks',NULL),
(5,'djarosz','Dariusz','Jarosz',NULL);
UNLOCK TABLES;

