import json 
raw_data = [1.82, 0.0, 1.85, None, 1.90, 1.78, 0.0 , 2.00 , 1.70, 2.2 , 1.10]
print(f"Αρχικά δεδομένα {raw_data}")

clean_data = []


for p in raw_data:
    if p is not None and p > 0:
        clean_data.append(p)
        
print(f"Η πραγματική καθαρισμένη λίστα είναι η {clean_data}")

count= len(clean_data)


if count > 0 :
    average = sum(clean_data) / count
    min_price = min(clean_data)
    max_price = max (clean_data)

else : 
    average = 0
    min_price = 0
    max_price = 0
    
print(f"Η μέση τιμή είναι {average}")



limit = 1.85

if average > limit :
    status_msg = "High prices"
else:
    status_msg = "Normal prices"



report = {
    "status": "success",
    "metadata": {
        "total_scraped" : len(raw_data),
        "valid_entries" : count ,
        "error_found": len(raw_data) - count
    },
    "data" : {
        "prices" : clean_data,
        "average_price": round(average,3),
        "min_price" : min_price,
        "max_price" : max_price,
        "alert_level": status_msg
    }
    
}



json_data=json.dumps(report, indent=4)
print(json_data)


with open("data.json", "w" , encoding="utf-8") as f:
    json.dumps(report, f, indent=4, ensure_ascii=False)
    
print("ok")
    
