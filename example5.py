import json 
raw_data = [1.82, 0.0, 1.85, None, 1.90, 1.78, 0.0 , 2.00]
print(f"Αρχικά δεδομένα {raw_data}")

clean_data = []


for p in raw_data:
    if p is not None and p > 0:
        clean_data.append(p)
        
print(f"Η πραγματική καθαρισμένη λίστα είναι η {clean_data}")

count= len(clean_data)


if count > 0 :
    average = sum(clean_data) / count

else : 
    average = 0
    
print(f"Η μέση τιμή είναι {average}")


report = {
    "status": "success",
    "metadata": {
        "total_scraped" : len(raw_data),
        "valid_entries" : count ,
        "error_found": len(raw_data) - count
    },
    "data" : {
        "prices" : clean_data,
        "average_price": round(average,3)
    }
    
}



json_data=json.dumps(report, indent=4)
print(json_data)
