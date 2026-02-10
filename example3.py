def compare_prices (price_list , liters):
    costs = []
    
    for price in prices:
        total = price*liters
        costs.append(round(total,2))
        
    return costs
    

def compare_max_min_prices (price_list , liters):
    max_price = max(price_list)
    min_price = min(price_list)
    cost_expensive= max_price * liters
    cost_cheap = min_price * liters
    difference_price = cost_expensive - cost_cheap
    return round(difference_price,2)
    
    
prices= [1.85 , 1.92, 1.78, 1.95, 1.82]

my_liters = 50 

all_costs = compare_prices(prices,my_liters)

print(f"Οι τιμές των λίτρων είναι: {prices}")
print(f"Το συνολικό κόστος είναι για {my_liters} λίτρα : {all_costs} euro")

saving = compare_max_min_prices(prices, my_liters)

print(f"Εαν επιλέξεις το φτηνότερο πρατήριο σε κάθε γέμισα έχεις κέρδος {saving} euro ")
