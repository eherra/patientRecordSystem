CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    is_doctor BOOLEAN
);

CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    key TEXT UNIQUE,
    value TEXT
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES users,
    doctor_id INTEGER REFERENCES users,
    time_at TIMESTAMP,
    appointment_type TEXT, 
    symptom TEXT DEFAULT ''
);

CREATE TABLE prescriptions (
    id SERIAL PRIMARY KEY,
    name TEXT,
    amount_per_day INTEGER
);

CREATE TABLE user_prescriptions (
    id SERIAL PRIMARY KEY,
    prescription_id INTEGER REFERENCES prescriptions,
    user_id INTEGER REFERENCES users,
    visible BOOLEAN DEFAULT TRUE
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user1_id INTEGER REFERENCES users,
    user2_id INTEGER REFERENCES users,
    content TEXT,
    sent_at TIMESTAMP
);