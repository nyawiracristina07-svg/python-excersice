number = input ("write a three digit number:")

hundreds = int(number) // 100
print(hundreds)
tens = (int(number) % 100) // 10
print(tens)
digit = (int(number) % 100) % 10 
print(digit)

sum = hundreds + tens + digit 
print(sum)
