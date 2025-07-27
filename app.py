from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import json, os

app = Flask(__name__)
DATA_FILE = 'harshini.json'

def load_medicines():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_medicines(meds):
    with open(DATA_FILE, 'w') as f:
        json.dump(meds, f, indent=4)

medicines = load_medicines()

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    data = request.get_json()
    required = ['name', 'batch_no', 'id','stock', 'expiry_date', 'category','available_stock','price']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400
    medicines.append(data)
    save_medicines(medicines)
    return jsonify({'message': 'Medicine added'}), 201

@app.route('/medicines', methods=['GET'])
def get_medicines():
    return jsonify(medicines), 200


@app.route('/low_stock', methods=['GET'])
def low_stock():
    threshold = 100 #  default value directly in code
    low = [
        m for m in medicines
        if m.get('stock') == "In Stock" and int(m.get('available_stock', 0)) < threshold
    ]
    return jsonify(low), 200


@app.route('/expiring_soon', methods=['GET'])
def expiring_soon():
    today = datetime.now().date()
    soon = today + timedelta(days=30)
    expiring = []
    for m in medicines:
        try:
            expiry = datetime.strptime(m['expiry_date'], "%Y-%m-%d").date()
            if today <= expiry <= soon:
                expiring.append(m)
        except:
            continue
    return jsonify(expiring), 200

#  Correct condition to run Flask app
if __name__ == '__main__':
    app.run(debug=True)
