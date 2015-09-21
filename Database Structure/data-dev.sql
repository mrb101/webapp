CREATE TABLE _module1 (
	id INTEGER NOT NULL, 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL
);
CREATE TABLE brands (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	slug VARCHAR(255) NOT NULL, 
	description VARCHAR(255), 
	active BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (slug), 
	CHECK (active IN (0, 1))
);
CREATE TABLE categories (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	slug VARCHAR(255) NOT NULL, 
	description VARCHAR(255), 
	parent INTEGER, 
	active BOOLEAN, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	CHECK (active IN (0, 1))
);
CREATE TABLE option_attributes (
	id INTEGER NOT NULL, 
	value VARCHAR(255) NOT NULL, 
	created_at DATETIME, 
	option_type_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(option_type_id) REFERENCES option_types (id)
);
CREATE TABLE option_types (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	created_at DATETIME, 
	product_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES products (id)
);
CREATE TABLE options (
	id INTEGER NOT NULL, 
	created_at DATETIME, 
	variation_id INTEGER, 
	option_attribute_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(option_attribute_id) REFERENCES option_attributes (id), 
	FOREIGN KEY(variation_id) REFERENCES variations (id)
);
CREATE TABLE password_reset (
	id INTEGER NOT NULL, 
	email VARCHAR(255) NOT NULL, 
	token VARCHAR(255) NOT NULL, 
	created_at DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE products (
	id INTEGER NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	slug VARCHAR(255) NOT NULL, 
	description TEXT(255), 
	active BOOLEAN, 
	created_at DATETIME, 
	category_id INTEGER, 
	brand_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(brand_id) REFERENCES brands (id), 
	FOREIGN KEY(category_id) REFERENCES categories (id), 
	UNIQUE (slug), 
	CHECK (active IN (0, 1))
);
CREATE TABLE users (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	user_name VARCHAR(20) NOT NULL, 
	email VARCHAR(255) NOT NULL, 
	password_hash VARCHAR(255), 
	created_at DATETIME, admin BOOLEAN, bio TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE variations (
	id INTEGER NOT NULL, 
	barcode INTEGER, 
	sku VARCHAR(255) NOT NULL, 
	name VARCHAR(255) NOT NULL, 
	price NUMERIC, 
	cost NUMERIC, 
	stock_level INTEGER, 
	weight NUMERIC, 
	height NUMERIC, 
	width NUMERIC, 
	length NUMERIC, 
	master BOOLEAN, 
	image VARCHAR(255), 
	created_at DATETIME, 
	product_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES products (id), 
	UNIQUE (barcode), 
	CHECK (master IN (0, 1))
);
CREATE UNIQUE INDEX ix_categories_slug ON categories (slug);
CREATE INDEX ix_password_reset_email ON password_reset (email);
CREATE INDEX ix_password_reset_token ON password_reset (token);
CREATE UNIQUE INDEX ix_users_email ON users (email);
CREATE UNIQUE INDEX ix_users_user_name ON users (user_name);
CREATE UNIQUE INDEX ix_variations_sku ON variations (sku);
