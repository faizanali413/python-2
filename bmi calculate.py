weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi= (weight/height**2)
print("The BMI is:", bmi)
if bmi < 18.5:
    print("According to the BMI scale, you are: Underweight")
elif 18.5 <= bmi < 24.9:
    print("According to the BMI scale, you are: Normal weight")
elif 24.9 <= bmi < 29:
    print("According to the BMI scale, you are: Overweight")
else:
    print("According to the BMI scale, you are: Obesity")