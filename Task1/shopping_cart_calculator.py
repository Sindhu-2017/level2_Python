# 5. Shopping Cart Calculator  

# Given multiple product prices: 

# Enter number of products: 5 

# Accept the prices using a loop. 

# Calculate: 

# Subtotal  

# Discount  

# Tax  

# Final amount  
 
# Apply different discounts based on the subtotal. 

product_count = int ( input ("Enter number of products :"))

prices = []

for i in range (0,product_count) :
    price = float ( input ("Enter the price :"))
    prices .append(price)

subtotal = sum (prices)

if subtotal >= 5000 :
    discount = subtotal * 0.10
elif subtotal >= 3000 :
    discount =subtotal * 0.05
else:
    discount = 0

total = subtotal - discount
tax = total * 0.05
final_amount = total + tax

print ( "Number of products :" , product_count )
print ( "Subtotal :" , subtotal )
print ( "Total amount after discount :" ,total)
print ( "Tax amount :" ,tax)
print ("Final amount :" ,final_amount)