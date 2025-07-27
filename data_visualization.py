#data visualization
import json
import matplotlib.pyplot as plt
from collections import Counter

DATA_FILE = 'harshini.json'

# Load medicine data
with open(DATA_FILE, 'r') as f:
    data = json.load(f)

# Bar Chart : Stock Levels 
names = [m['name'] for m in data[:10]]  # Top 10 for visibility
stocks = [int(m['available_stock']) for m in data[:10]]

plt.figure(figsize=(10, 5))
plt.bar(names, stocks, color='skyblue')
plt.title("Top 10 Medicine Stock Levels")
plt.xlabel("Medicine Name")
plt.ylabel("Available Stock")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#pie chart : Category Distribution
categories = [m['category'] for m in data]
category_counts = Counter(categories)

plt.figure(figsize=(6, 6))
plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Medicine Category Distribution")
plt.tight_layout()
plt.savefig("pie_chart.png") 
plt.show()  