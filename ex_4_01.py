amount = input ("give me the amount:")
amount_interger = (int(amount))

fifty_euros = amount_interger // 50
print(f" 50 euros: {fifty_euros}")

reminder_twenty_euros = (amount_interger % 50)
twenty_euros = reminder_twenty_euros // 20
print(f" 20 euros: {twenty_euros}")

reminder_ten_euros = (reminder_twenty_euros % 20)
ten_euros = reminder_ten_euros // 10
print(f" 10 euros: {ten_euros}")

reminder_five_euros = (reminder_ten_euros % 10)
five_euros = (reminder_five_euros % 10) // 5
print(f" 5 euros: {five_euros}")

reminder_two_euros = (reminder_five_euros % 5)
two_euros = (reminder_two_euros % 5) // 2
print(f" 2 euros: {two_euros}")

reminder_one_euros = (reminder_two_euros % 2)
one_euro = (reminder_one_euros % 2) // 1
print(f" 1 euro: {one_euro}")





