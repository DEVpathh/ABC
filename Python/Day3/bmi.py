#bmi calculator
weight = float(input("WHat is your weight in kg?"))
height = float(input("What is your height in meters?"))
bmi = weight/(height**2)
print(f"Your bmi is {bmi}kg/m^2")
if bmi<18.5:
    print("You are underweigth")
elif bmi>24.9:
    print("You are overweight")
else:
    print("You are normal")