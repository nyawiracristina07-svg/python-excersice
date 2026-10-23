unit_price_1 = input("please give me the unit price 1:")
unit_price_2 = input("please give me the unit price 2")
quantity1 = input ("please give me quantity of the first item:")
quantity2 = input("please give me quantity of the second item:")

total_without_tax = (float(quantity1) * float(unit_price_1)) +  (float(quantity2) * float(unit_price_2))
print(total_without_tax)
total_with_tax  =  ( 40 / 100 * total_without_tax) + total_without_tax
print(round(total_with_tax,2))

print ("-" * 30)
print (f"    {round(total_with_tax,2)} {round(total_without_tax,2)}   ")
print ("-" * 30)



