print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#calculate tip amount
tip_amount = round(bill * (tip / 100), 2)

#calculate total bill
total_bill = bill + tip_amount

#calculate what each has to pay for the total bill
bill_split = round((total_bill / people), 2)

#calculate what each has to pay for the tip
tip_per_person = round ((tip_amount / people), 2)

print(f"Total tip costs ${tip_amount}")
print(f"Total bill costs ${total_bill}")
print(f"Each pays ${bill_split} of bill")
print(f"Each pays ${tip_per_person} of tip")