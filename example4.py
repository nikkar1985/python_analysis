import json

history = [
    {"date":  "2026-02-01", "price": 1.82},
    {"date": "2026-02-02", "price": 1.85},
    {"date": "2026-02-03", "price": 1.84},
    {"date": "2026-02-04", "price": 1.88},
    {"date": "2026-02-05", "price": 1.90},
    {"date": "2026-02-06", "price": 1.87},
    {"date": "2026-02-07", "price": 1.89},
    {"date": "2026-02-08", "price": 1.89},
    {"date": "2026-02-09", "price": 2.00},
    {"date": "2026-02-10", "price": 1.80}
    ]
    
    
print(len(history))    
print(f" Συλλέχθηκαν δεδομένα {len(history)} ημερων ")


print("########### Υπολογισμός ποσοστιαίας διαφοράς 2 τιμών #####")

current = history[-1]["price"]
previous = history[-2]["price"]

diff = current - previous
percentage_change = (diff/previous)*100

status = "Αύξηση" if diff > 0 else "Μείωση"


json_data=json.dumps(history, indent=4)
print(json_data)

print(f" Σήμερασ : {current } euro  Χτες {previous} euro ")
print(f"Τάση {status} με ποσοστο ({percentage_change:.2f}%) ")






    
