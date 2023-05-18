-- createreates the MySQL server user user_0d_1.
-- create usre
-- flushing priviledges
-- grant all priviledges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

FLUSH PRIVILEGES;

GRANT ALL  PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
