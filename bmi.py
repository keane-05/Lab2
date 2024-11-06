def calculate_bmi(height, weight): 
    print("Weight = " + str(weight))
    print("Height = ", str(height))
    bmi = weight / (height**2)
    print("Your BMI is ", round(bmi,2))
    print("Weight Classification: ", end = "")
    # use round(variable, dp), this is so that you can round to the nearest dp
    if bmi < 18.5: 
        print("You are underweight")
        return -1
    elif bmi >25.0:
        print("You are overweight")
        return 0 
    else: 
        print("You are Normal Weight")
        return 1

calculate_bmi(weight = 57, height = 1.73)
print("==========")
calculate_bmi(weight = 20, height = 1.73)
print("==========")
calculate_bmi(weight = 100, height = 1.73)
