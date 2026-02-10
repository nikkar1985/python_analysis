
prices= [1.85 , 1.92, 1.78, 1.95, 1.82]


print("Τιμές αμόλυβδης: ",prices) 
print("########")

count_manual=0

for price in prices :
    count_manual = count_manual + 1
    print(count_manual)

print("########")

count_manual=0

for price in prices :
    count_manual = count_manual + 1

print(count_manual)


    






print("########")


count = len(prices)
print("Τα βενζινάδικα είναι :", count)

print(prices[0])

min_price = prices[0]

for price in prices:
    if price < min_price:
        min_price=price
    
print(min_price)
print(f"Η ελάχιστη τιμή είναι: {min_price} euro")


max_price = prices[0]
for price in prices:
    if price > max_price:
        max_price=price

print(max_price)
print(f"Η μέγιστη τιμή είναι: {max_price} euro")

print("########")

max_price_new=max(prices)

print(max_price_new)

min_price_new = min(prices)
print(min_price_new)
print("########")
total_sum = 0
for price in prices:
    total_sum = total_sum+price
    print(total_sum)
print("########")
total_sum = 0
for price in prices:
    total_sum = total_sum+price
    
print(total_sum)

average_price = total_sum / count
print(average_price)
print(f"Μεση τιμη : {average_price} euro")
print(f"Μεση τιμη : {average_price:.2f} euro")
print("########")

new_average_price = sum(prices)/count
print(new_average_price)

print("########")

manual_counter_expensive = 0

for price in prices :
    if price > 1.82 :
        manual_counter_expensive = manual_counter_expensive + 1
        print(manual_counter_expensive)

print("########")

new_manual_counter_expensive = 0

for price in prices :
    if price > 1.82 :
        new_manual_counter_expensive = new_manual_counter_expensive + 1
print(f"Οι τιμές πάνω από 1.82 είναι {new_manual_counter_expensive}")

print("########")

manual_counter_cheap = 0
for price in prices :
    if price < 1.83:
        manual_counter_cheap = manual_counter_cheap+1
        print(manual_counter_cheap)
        
print("########")

manual_counter_cheap = 0
for price in prices :
    if price < 1.83:
        manual_counter_cheap = manual_counter_cheap+1

print(f" Οι τιμές κάτω απο 1.83 είναι {manual_counter_cheap} ")


print("########")


manual_counter_average_price = 0
for price in prices:
    if price == 1.82 :
        manual_counter_average_price = manual_counter_average_price + 1

print(f"Οι τιμές που έχουν 1.82 είναι {manual_counter_average_price}")
    
print("########")

manual_counter_average_not_equal = 0

for price in prices:
    if price != 1.82 :
        manual_counter_average_not_equal = manual_counter_average_not_equal +1
        
print(f"Οι τιμές που έχουν τιμή διάφορη του 1.82 είναι {manual_counter_average_not_equal}")
        
        
print("########")

new_manual_counter_expensive_new = 0

for price in prices :
    if price >= 1.82 :
        new_manual_counter_expensive_new = new_manual_counter_expensive_new + 1
print(f"Οι τιμές πάνω ή ίσον του 1.82 είναι {new_manual_counter_expensive_new}")

print("########")


new_manual_counter_expensive_new_new = 0

for price in prices :
    if price <= 1.82 :
        new_manual_counter_expensive_new_new = new_manual_counter_expensive_new_new + 1
print(f"Οι τιμές μικρότερες ή ίσον του 1.82 είναι {new_manual_counter_expensive_new_new}")

print("########")




