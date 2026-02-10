import json

prices= [1.85 , 1.92, 1.78, 1.95, 1.82]

average_price = sum(prices)/len(prices)

#Dictionary
dashboard_data= {
    "fuel_type":"Unleaded 95",
    "all_prices":prices,
    "average": round(average_price,3),
    "max" : max(prices),
    "min": min(prices),
    "is_expensive": average_price>1.85
}

#Μετατροπή σε JSON 
json_output = json.dumps(dashboard_data , indent = 4)

print(json_output)
