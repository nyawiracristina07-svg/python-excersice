bill = input("What is the bill:")
percentage_tip = input("What is the percentage tip?")
number_of_people = input("What are the number of people:")

number_of_people_float = int(number_of_people)
bill_float = float(bill)
tip_float =  (bill_float * float(percentage_tip)) / 100
#print(round(tip_float,2))
bill_total = bill_float + tip_float
#print(round(bill_total,2))
share_of_each_person = round(bill_total / number_of_people_float,2) 
#print(share_of_each_person)

group_total = (share_of_each_person * number_of_people_float) - bill_total
#print (round(group_total,2))

print ("="* 30)
print(f"Tip : {round(tip_float,2)}")
print(f"Total : {round(bill_total,2)}")
print(f"Each person pays : {share_of_each_person}")
print(f"Difference: {round(group_total,2)}")
print ("="* 30)

# the difference of having this input "100, 0, 3" is that rounding each persons share to two decimal places causes a difference of 0.01 in the bill meaniing they pay 0.01 less from the total bill
