#Restaurant Bill Spliter Program
print("----Restaurant Billing system----")
bill = float(input("Enter total bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = bill * tip_percent / 100
total_bill = bill + tip
per_person = total_bill / people

print("Total Tip:", tip)
print("Total Bill with Tip:", total_bill)
print("Each Person Pays:", per_person)
print("----Thanks for Comming!----")