CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

CREATE TABLE `user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `uid` varchar(255) COLLATE utf8_bin NOT NULL,
    `upw` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;


CREATE TABLE users (
    userid varchar(11) NOT NULL, 
    email varchar(255)  NOT NULL,
    address varchar(255),
    password varchar(255)  NOT NULL,
    PRIMARY KEY (userid)
 );

insert into users values('hong','hong@gmail.com','부산','1111');
insert into users values('hong','hong@gmail.com','부산','1111'); 