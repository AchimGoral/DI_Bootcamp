CREATE TABLE lib_user (
	user_id SERIAL PRIMARY KEY,
	email TEXT UNIQUE,
	first_name VARCHAR (50),
	last_name VARCHAR (50)
)

CREATE TABLE lib_store (
	user_id SERIAL PRIMARY KEY,
	books VARCHAR (30),
	story TEXT,
	pages SMALLINT,
	ISBN SMALLINT,
	FOREIGN KEY (user_id) REFERENCES lib_user(user_id) ON DELETE CASCADE
)

CREATE TABLE lib_rents (
	lib_store_user_id SERIAL,
	FOREIGN KEY (lib_store_user_id) REFERENCES lib_store(user_id) ON DELETE CASCADE,
	lib_user_id SERIAL PRIMARY KEY,
	FOREIGN KEY (lib_user_id) REFERENCES lib_user(user_id) ON DELETE CASCADE,
	rental_date DATE
)

INSERT INTO lib_user (email, first_name, last_name)
VALUES
('Jon.doe@gmail.com', 'Jon', 'Doe'),
('Mikeee@gmail.com', 'Mike', 'Michaelson'),
('janina@gmail.com', 'Janina', 'Smith'),
('Waine123@yahoo.com', 'Waine', 'Dwight')

INSERT INTO lib_store (books, story, pages, isbn)
VALUES
('Harry Potter', 'Wizard uses magiv to defend his parents killer', 325, 548),
('The Hobbit', 'Bilbo on a journey to kill the dragon', 1250, 789),
('Developers', 'People sit hours daily to learn databases and stuff', 1045, 411)

INSERT INTO lib_rents (lib_store_user_id, lib_user_id, rental_date)
VALUES
(1, 1, '13/01/2021'),
(1, 2, '10/02/2021'),
(2, 3, '01/02/2021'),
(3, 1, '08/02/2021'),
(3, 3, '07/02/2021'),
(3, 4, '02/02/2021')