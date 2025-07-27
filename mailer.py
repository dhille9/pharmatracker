#mailer.py
import json
import smtplib
from datetime import datetime, timedelta

# File that stores medicine data
file_name = 'harshini.json'

# Your Gmail details
my_email = "your_email@gmail.com"
my_password = "your_app_password"
send_to = "receiver_email@gmail.com"

# Load all medicines from JSON file
def get_medicines():
    with open(file_name, 'r') as f:
        return json.load(f)

# Check which medicines will expire in the next 30 days
def find_expiring_medicines():
    today = datetime.today().date()
    next_30_days = today + timedelta(days=30)

    medicines = get_medicines()
    message = "Medicines expiring in the next 30 days:\n\n"
    found = False

    for med in medicines:
        try:
            expiry = datetime.strptime(med['expiry_date'], "%Y-%m-%d").date()
            if today <= expiry <= next_30_days:
                message += f"{med['name']} - Batch {med['batch_no']} - Expiry: {med['expiry_date']}\n"
                found = True
        except:
            continue


    if found:
        print(message)
        send_email(message)
    else:
        print("No medicines are expiring in the next 30 days.")

# Send email using Gmail
def send_email(content):
    subject = "Medicine Expiry Alert"
    email_text = f"Subject: {subject}\n\n{content}"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(my_email, my_password)
        server.sendmail(my_email, send_to, email_text)
        server.quit()
        print("Email sent successfully.")
    except Exception as error:
        print("Error sending email:", error)

# Run the check when file is executed
if __name__ == "__main__":
    find_expiring_medicines()
