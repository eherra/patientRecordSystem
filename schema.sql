CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    isDoctor BOOLEAN
);

CREATE TABLE UserInfo (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    key TEXT,
    value TEXT
);

CREATE TABLE Appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Users,
    doctor_id INTEGER REFERENCES Users,
    time_at TIMESTAMP,
    appointment_type TEXT, 
    symptom TEXT
);

CREATE TABLE Prescriptions (
    id SERIAL PRIMARY KEY,
    name TEXT,
    amount_per_day INTEGER
);

CREATE TABLE UserPrescriptions (
    id SERIAL PRIMARY KEY,
    prescription_id INTEGER REFERENCES Prescriptions,
    user_id INTEGER REFERENCES Users,
    visible BOOLEAN DEFAULT TRUE
);

CREATE TABLE Messages (
    id INTEGER PRIMARY KEY,
    user1_id INTEGER REFERENCES Users,
    user2_id INTEGER REFERENCES Users,
    content TEXT,
    sent_at TIMESTAMP
);
