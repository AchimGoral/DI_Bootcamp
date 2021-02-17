create table orders (
	order_id serial primary key,
)

--

create table items (
	item_id serial primary key,
	item varchar(30) not null,
	price integer not null,
)

-- 

create table finals (
	order_id integer not null,
	item_id integer not null,
	foreign key (order_id) 
	references orders (order_id)
	on delete cascade,
	foreign key (item_id) 
	references items (items_id)
	on delete cascade,
)