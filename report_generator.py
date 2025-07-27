#report generator
from reportlab.pdfgen import canvas
import json

def create_pdf(data, filename="medicine_report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 800, "Medicine Report")
    c.setFont("Helvetica", 10)

    y = 770
    for m in data:
        line = f"{m['name']} | Batch: {m['batch_no']} | Stock: {m['available_stock']} | Expiry: {m['expiry_date']}"
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 800

    c.save()
    print(f" PDF saved as {filename}")

if __name__ == "__main__":
    # Point to the uploaded file location
    file_path = r"C:\Users\siri\Desktop\my project\harshini.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    create_pdf(data)
