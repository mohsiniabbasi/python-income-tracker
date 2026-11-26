import json
import sqlite3

db = sqlite3.connect('tracker.db')

f = open("entries.json", "r")
entries = json.load(f)
f.close()

for e in entries:
    db.execute("INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?)", (e["date"], e["week"], e["tax_year"], e["income"], e["expenses"], e["profit"]))

f = open("entries-costs.json", "r")
costs = json.load(f)
f.close()

for c in costs:
        db.execute("INSERT INTO costs VALUES (?, ?, ?)", (c["tax_year"], c["name"], c["amount"]))
        
db.commit()
print("Data copied to database successfully.", len(entries), "entries and", len(costs), "costs added.")
