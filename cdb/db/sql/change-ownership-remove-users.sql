-- Execute by running `~/cdb-support/bin/mysql-client-cdb < change-ownership-remove-users.sql`

-- Changes all cdb item ownership to user "cdb" and removes all other named users.
-- Assumes that cdb user id in user_info table = 1.

delete from user_role where user_id != 1;
update entity_info set owner_user_id = 1;
update entity_info set created_by_user_id = 1;
update entity_info set last_modified_by_user_id = 1;
update item_element_relationship_history set entered_by_user_id = 1;
update log set entered_by_user_id = 1;
update property_value set entered_by_user_id = 1;
update property_value_history set entered_by_user_id = 1;
delete from user_list where user_id != 1;
delete from user_info where id != 1;

