DROP TABLE IF EXISTS `user` ;


create table user
(
  id   int auto_increment
    primary key,
  name varchar(255) not null,
  password varchar(255) not null,
  phone    varchar(255) not null
)
  charset = utf8;