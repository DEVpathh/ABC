#pythin pizza deliveries
print("Welcome to the pizza deliveries")
size = input("What size of pizza do you want?S, M or L\n")


bill = 0
if size == 'S':
    bill = 15
   
elif size == 'M':
    bill = 20
   
elif size == 'L':
    bill = 25

pepperoni = input("Do you want peperonies on it?Y or N\n")
if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3 
cheeze = input("do you want Extra cheeze?Y or N\n")   
if cheeze == 'Y':
    bill += 1
    print(f"your total bill is ${bill}")


else:
    print(f"Yor total bill is ${bill}")