create database highlow;
use highlow;

create table high_low(
	ID int PRIMARY KEY AUTO_INCREMENT,
	SYMBOL varchar(5),
	HIGH float,
	LOW float
	);