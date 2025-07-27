#analytics
import json
from datetime import datetime
from collections import Counter

DATA_FILE = 'harshini.json'

def load_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def analyze():
    data = load_data()
    total = len(data)
    low_stock = [m for m in data if int(m['available_stock']) <= 5]
    expired = []
    today = datetime.today().date()
    categories = []

    for med in data:
        try:
            exp = datetime.strptime(med['expiry_date'], "%Y-%m-%d").date()
            if exp < today:
                expired.append(med)
        except:
            continue
        categories.append(med['category'])

    print("PharmaTracker – Inventory Analytics")
    print("--------------------------------------")
    print(f" Total medicines: {total}")
    print(f"Low stock medicines (<=5): {len(low_stock)}")
    print(f"Expired medicines: {len(expired)}")

    if categories:
        top = Counter(categories).most_common(3)
        print("Top categories:")
        for cat, count in top:
            print(f" - {cat}: {count} items")

if __name__ == '__main__':
    analyze()
