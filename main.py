print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people are sharing the bill? "))
tip = float(input("What percentage of tip would you like to leave? "))
bill_with_tip = bill*(1+tip/100)
bill_per_person = bill_with_tip/num_of_people

#rounding bill to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")