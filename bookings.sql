CREATE TABLE bookings (
    id INT NOT NULL AUTO_INCREMENT,
    restaurant_id INT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    number_of_guests INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
);
