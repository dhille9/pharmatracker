Pharmatracker
================

Project by: Dhilleswararao Boddepalli  
Email: dhille99@gmail.com  

Overview:
---------
Pharmatracker is a lightweight backend application built with Python and Flask to manage medicine inventory and track expiry dates efficiently. It generates reports, sends alerts, and provides clean API endpoints for further integration.

Key Features:
-------------
Add, retrieve, and filter medicine data  
Track low stock and upcoming expiries  
JSON-based data storage (no database required)  
PDF report generation using ReportLab  
Visualize stock and category data using matplotlib  
API tested with Postman

Tech Stack:
-----------
- Python 3.8+
- Flask (backend framework)
- ReportLab (PDF generation)
- Postman (API testing)
- matplotlib (charts & graphs)

Folder Structure:
-----------------
Pharmatracker/
├── app.py                  → Main Flask application  
├── models.py               → (Optional) Data structures  
├── scheduler.py            → (Optional) Scheduler for expiry checking  
├── mailer.py               → Email/alert functionality  
├── report_generator.py     → PDF report creation (ReportLab)  
├── analytics.py            → Medicine stock/expiry analysis  
├── data_visualization.py   → Visual reports using matplotlib  
├── data.json               → JSON file storing medicine records  
├── requirements.txt        → Project dependencies  
└── README.txt              → Project documentation (this file)

How to Run:
-----------
1. Install dependencies:
   pip install -r requirements.txt

2. Start the Flask server:
   python app.py

3. Use Postman to test APIs or integrate with any frontend.

Sample API Endpoints:
---------------------
- POST /add_medicine → Add a new medicine record  
- GET /medicines → Retrieve all records  
- GET /low_stock?threshold=10 → Get medicines below stock threshold  
- GET /expiring_soon → List medicines expiring in the next 30 days  

Future Enhancements:
--------------------
- Add user authentication  
- Integrate email notifications for expiry  
- Move to database (e.g., SQLite or MongoDB)  
- Build a React/HTML frontend  
- Enable barcode scanning for batch numbers

License:
--------
This is an academic project created for learning and demonstration purposes.
