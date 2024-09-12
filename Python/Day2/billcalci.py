print("Welcome to the bill calculator")
total_bill= float(input("What is the total bill?\n$"))
perc = float(input("How much percentage you want to tip? 10 12 or 15\n"))
div = int(input("How many people are there?\n"))
final_bill = (total_bill+perc/100)/div
round_bill = round(final_bill,2)
print(f"The total bill is ${round_bill}")