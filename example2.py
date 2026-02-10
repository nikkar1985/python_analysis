def calculate_range (price_list):
    highest = max(price_list)
    lowest = min(price_list)
    
    diff = highest - lowest 
    
    return diff
    
prices= [1.85 , 1.92, 1.78, 1.95, 1.82]

range_value = calculate_range(prices)


print(range_value)

print(f"{range_value:.2f}")


def cost(price , liters):
    total_cost= price*liters
    return round(total_cost,2)
    
my_liters = 40
gas_price = 2

final_cost = cost (2,40)

print(f"Για να γεμίσει το ρεζερβουάρ θέλει {my_liters} λίτρα με κόστος {gas_price} euro και συνολικό κόστοw {final_cost} euro")    
