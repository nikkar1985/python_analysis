import json

products = [
    {"shop" : "Plaisio", "price" : 1250},
    {"shop" : "Kotsovolos", "price" : 1180},
    {"shop" : "Public", "price" : 1300},
    {"shop" : "Cosmodata", "price" : 1150},
    {"shop" : "Megastore", "price" : 1210},
    {"shop" : "Jumbo", "price" : 1500},
    {"shop" : "Mall", "price" : 1000},
    {"shop" : "AB", "price" : 1100},
    {"shop" : "Metro", "price" : 1600}
]

best_deal = products[0]
max_product = products[0]



for p in products:
    if p['price'] < best_deal['price']:
        best_deal = p  
    if p['price'] > max_product['price']:
        max_product = p 

max_price=max_product['price']
price_gap=((max_price - best_deal['price'])/ best_deal['price'])*100



analysis_report = {
    "recommendation": {
        "best_shop": best_deal['shop'],
        "best_price": best_deal['price'],
        "potentional_saving": max_price - best_deal['price']
    },
    "market_stats" : {
        "total_shops":len(products),
        "cost_shop": max_product['shop'], 
        "max_price": max_product['price'],
        "percentage difference": round(price_gap, 2)
    }
}

json_data = json.dumps(analysis_report, indent=4)
print(json_data)
