Clinic Booking System API
A simple RESTful API for managing patients, doctors, and appointments in a clinic.
Built using FastAPI, SQLAlchemy, and SQLite.

Features
Create, retrieve, update, and delete patient records.

Future-ready for doctor and appointment management.

Database setup with SQLAlchemy ORM.

Auto-generated documentation via Swagger UI and ReDoc.

Technologies Used
FastAPI — for building APIs quickly and efficiently.

SQLAlchemy — for ORM-based database interactions.

SQLite — as the database for simplicity.

Pydantic — for request validation and response serialization.


SQL Script
The create_database.sql file contains the SQL code used to create the database tables manually.

ERD (Entity-Relationship Diagram)
You can view the ERD diagram here:
📎 [(https://1drv.ms/i/c/2bb2f9afc8ae1149/EZTv_XSFX1VCu8FN44OHd5wBH-S861J8-p6PwUCHFFhJZQ?e=qLY05R)]


Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/Cynthia-M-M/clinic-booking-system-api.git
Navigate into the Project Directory

bash
Copy
Edit
cd clinic-booking-system-api
Create and Activate a Virtual Environment

bash
Copy
Edit
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
Install the Requirements

bash
Copy
Edit
pip install -r requirements.txt
Running the Application
Start the FastAPI development server:

bash
Copy
Edit
uvicorn app.main:app --reload
The API will be available at: http://127.0.0.1:8000

Interactive Swagger Docs: http://127.0.0.1:8000/docs

ReDoc Documentation: http://127.0.0.1:8000/redoc

Project Structure
bash
Copy
Edit
clinic-booking-system-api/
│
├── app/
│   ├── database/
│   │   └── database.py        # Database setup
│   ├── models/
│   │   └── models.py           # SQLAlchemy models
│   ├── schemas/
│   │   └── schemas.py          # Pydantic schemas
│   └── main.py                 # Main application routes
│
├── env/                        # Virtual environment (not pushed to GitHub)
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
API Endpoints

Method	Endpoint	Description
POST	/patients/	Create a new patient
GET	/patients/	Get all patients
GET	/patients/{patient_id}	Get a single patient by ID
PUT	/patients/{patient_id}	Update a patient by ID
DELETE	/patients/{patient_id}	Delete a patient by ID
Notes
Currently, the focus is on patients.

Future improvements can add doctor and appointment management.

License
This project is open for educational use.

Author
Cynthia M.