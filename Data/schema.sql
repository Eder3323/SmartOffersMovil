CREATE DATABASE kuorra_login;

USE kuorra_login;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    shopping_chain_status integer NOT NULL DEFAULT 0,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE discount_types(
    id_discount_type integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    description text(150) NOT NULL,
    value double NOT NULL,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE company_types(
    id_company_types integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    description text(150) NOT NULL,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE companies(
    id_company integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    description text(150) NOT NULL,
    owner varchar(20) NOT NULL,
    type integer NOT NULL,
    address text(150) NOT NULL,
    FOREIGN KEY (owner) REFERENCES users(username),
    FOREIGN KEY (type) REFERENCES company_types(id_company_types),
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE offers(
    id_offer integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    description text(150) NOT NULL,
    creator varchar(20) NOT NULL,
    product_name varchar(30) NOT NULL,
    price double NOT NULL,
    discount_value integer NOT NULL, 
    new_price double NOT NULL,
    FOREIGN KEY (creator) REFERENCES users(username),
    FOREIGN KEY (discount_value) REFERENCES discount_types(id_discount_type),
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE shopping_chains(
    id_shopping_chain integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    client varchar(20) NOT NULL,
    offer integer NOT NULL, 
    status integer NOT NULL default 0,
    creator varchar(20) not null,
    limited_time double NOT NULL,
    FOREIGN KEY (client) REFERENCES users(username),
    FOREIGN KEY (creator) REFERENCES users(username),
    FOREIGN KEY (offer) REFERENCES offers(id_offer),
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;




INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'kuorra'@'localhost' IDENTIFIED BY 'kuorra.2018';
GRANT ALL PRIVILEGES ON kuorra_login.* TO 'kuorra'@'localhost';
FLUSH PRIVILEGES;
