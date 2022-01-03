use datarepresentation;

create table stock_close(
	ID int PRIMARY KEY AUTO_INCREMENT,
	SYMBOL varchar(5),
	OPEN float,
	CLOSE float,
	VOLUME float
	);