CREATE DATABASE IF NOT EXISTS clinic_db;
-- Question 1
USE clinic_db;
-- CREATE Patients Table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    date_of_birth DATE,
    address TEXT
);
-- CREATE Doctors Table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    years_of_experience INT DEFAULT 0
);

-- CREATE Appointments Table
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_datetime DATETIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
);

-- Insert Real Patients
INSERT INTO patients (full_name, email, phone_number, date_of_birth, address) VALUES
('Emma Watson', 'emma.watson@example.com', '0700123456', '1990-04-15', '123 Elm Street, Nairobi'),
('James Bond', 'james.bond@example.com', '0700987654', '1985-11-23', '456 Pine Street, Nairobi');

-- Insert Real Doctors
INSERT INTO doctors (full_name, specialization, phone_number, email, years_of_experience) VALUES
('Dr. Catherine Mwangi', 'Cardiology', '0711223344', 'catherine.mwangi@clinic.com', 10),
('Dr. Kevin Otieno', 'Pediatrics', '0722334455', 'kevin.otieno@clinic.com', 7);

-- Insert Real Appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_datetime, status, notes) VALUES
(1, 1, '2025-05-15 10:00:00', 'Scheduled', 'Regular heart checkup'),
(2, 2, '2025-05-16 09:30:00', 'Scheduled', 'Child vaccination follow-up');

-- To Verify
USE clinic_db;
SELECT * FROM patients;
SELECT * FROM patients;
SELECT * FROM doctors;
SELECT * FROM appointments;
