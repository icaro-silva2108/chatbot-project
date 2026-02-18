CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) Engine=InnoDB;

CREATE TABLE destinations (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
	img_url VARCHAR(255) NOT NULL
)Engine=InnoDB;

CREATE TABLE reservations(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    travel_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
	CONSTRAINT fk_reservation_user
		FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
	CONSTRAINT fk_reservations_destinations
		FOREIGN KEY (destination_id)
        REFERENCES destinations(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
)Engine=InnoDB;
