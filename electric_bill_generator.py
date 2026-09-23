# 4. Electricity Bill Generator
#
# Input:
#
# Customer Name
#
# Units Consumed
#
# Calculate the bill using slabs.
#
# Also display:
#
# Customer Name
#
# Units Consumed
#
# Energy Charge
#
# Tax
#
# Total Bill
#
# Handle invalid/negative units.

customer_name = input ("Enter the customer name :")
unit_consumed = int(input("Enter value of units consumed :"))

if unit_consumed < 0 :
    print("Units cannot be negative ")

else :
    if unit_consumed <= 100 :
        energy_charge = 0

    elif unit_consumed <= 200 :
        energy_charge = ( unit_consumed - 100 ) * 2.25

    elif unit_consumed <= 500 :
        energy_charge = ( 100 * 0 ) + ( 100 * 2.25 ) + ( unit_consumed - 200 ) * 4.5

    else:
        energy_charge = ( 100 * 0 ) + ( 100 * 2.25) + ( 300 * 4.5 ) + ( unit_consumed - 500 ) * 6

tax = energy_charge * 0.05
total_bill = energy_charge + tax

print ( "Customer Name :",customer_name )
print ( "Units Consumed :" , unit_consumed)

print ( "Energy Charge :" ,energy_charge)
print ("Tax :",tax)
print ( "Total bill :" ,total_bill)


