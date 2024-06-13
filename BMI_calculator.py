name = input("Enter your name to calculate BMI: ")
height = float(input("Enter your height in centimeter: "))
weight = float(input("Enter your weight in kilograms: "))

height1 = height/100

BMI = weight/(height1**2)

print(f"Name: {name}")
print(f"Height: {height} cm")
print(f"Weight: {weight} kg")
print(f"{name},your Body Mass Index is..")

if BMI>0:
    
    if BMI<=16:
        print(f"Your BMI is {BMI:0.2f} hence you are Severely Underweight")
        
    elif BMI<=18.5:
        print(f"Your BMI is {BMI:0.2f} hence you are Underweight")
        
    elif BMI<=25:
        print(f"Your BMI is {BMI:0.2f} hence you are Healthy")
        
    elif BMI<=30:
        print(f"Your BMI is {BMI:0.2f} hence you are Overweight")
        
    elif BMI<=34.9:
        print(f"Your BMI is {BMI:0.2f} hence you are Obesity")
        
    elif BMI>35:
        print(f"Your BMI is {BMI:0.2f} hence you are Extremely Obese")
        
else:
    print("Please enter the correct detials")