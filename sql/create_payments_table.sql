CREATE TABLE IF NOT EXISTS payments (
    payment_id VARCHAR PRIMARY KEY,
    customerID VARCHAR,
    payment_date DATE,
    amount FLOAT,
    payment_method VARCHAR,
    payment_status VARCHAR
);
