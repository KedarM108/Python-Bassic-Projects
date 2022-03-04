'''If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to 24.9, it falls within the normal or Healthy Weight range.
If your BMI is 25.0 to 29.9, it falls within the overweight range.'''


print("****************** BMI CALCULATOR ******************")

age = input("Enter your current age: ")

weight = float(input("Enter your weight (in kgs): "))

height = float(input("Enter your height (in meters): "))

bmi = weight / ( height ** 2 )
print("Your BMI = ",bmi)

if bmi>25.0:
    print(" OVERWEIGHT ")
elif bmi<18.5:
    print(" UNDERWEIGHT ")
else:
    print(" HEALTHY WEIGHT")

