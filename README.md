PharmaTracker 
A lightweight Python + Flask application to manage medicines, track expiry, send alerts, generate PDF reports, and visualize inventory.

 Features
 Add and view medicines using REST API
 Alerts for medicines expiring in next 30 days
 Detect low stock (threshold-based)
 Generate PDF reports from data
 Visualize inventory using bar and pie charts
 Send email alerts via Gmail
 Data stored in JSON (no database used)

Folder Structure:
PharmaTracker/
├── app.py                  # Flask API backend
├── mailer.py               # Email alerts for expiry
├── scheduler.py            # Scheduled expiry checker
├── report_generator.py     # PDF report creation
├── analytics.py            # Medicine stats (stock, expired, category)
├── data_visualization.py   # Bar and pie charts
├── harshini.json           # Medicine data (JSON)
├── requirements.txt        # Required Python libraries
└── README.md               # This file
🔧 Setup Instructions
1. Install dependencies
pip install -r requirements.txt
2. Run the Flask API
python app.py
Test using Postman or browser:
GET /medicines
POST /add_medicine
GET /low_stock?threshold=5
GET /expiring_soon
3. Generate PDF report
python report_generator.py
4. Show charts (stock & category)
python data_visualization.py
5. Send expiry alerts to email
python mailer.py
 Make sure to set your Gmail & App Password inside mailer.py.
6. Check expiring medicines manually/scheduled
python scheduler.py
sample JSON Record (harshini.json)
{
  "id": 1,
  "name": "Paracetamol",
  "category": "Antipyretic",
  "batch_no": "PA2553",
  "expiry_date": "2026-05-21",
  "price": 8.41,
  "stock": "In Stock",
  "available_stock": 25
}
Technologies Used
Python 3.8+
Flask
JSON
ReportLab
Matplotlib
smtplib (Gmail SMTP)

 Author
Dhilleswararao Boddepalli
Email: dhille99@gmail.com
