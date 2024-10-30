def calculate_bmi(height, weight): 
    print("Weight = " + str(weight))
    print("Height = ", str(height))
    bmi = weight / (height**2)
    print("Your BMI is ", round(bmi,2))
    print("Weight Classification: ", end = "")
    # use round(variable, dp), this is so that you can round to the nearest dp
    if bmi < 18.5: 
        print("You are underweight")
    elif bmi >25.0:
        print("You are overweight")
    else: 
        print("You are Normal Weight")

calculate_bmi(weight = 57, height = 1.73)
print("==========")
calculate_bmi(weight = 57, height = 1.73)
print("==========")
calculate_bmi(weight = 57, height = 1.73)
