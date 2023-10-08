
# Function to calculate BMR (Basal Metabolic Rate)
def calculate_bmr(weight_kg, height_cm, age, gender):
    if gender == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Invalid gender")
    return bmr

# Function to calculate daily calorie needs based on BMR and activity level
def calculate_calories(bmr, activity_level):
    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'super_active': 1.9
    }
    return bmr * activity_factors[activity_level]

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ").lower()
activity_level = input("Enter your activity level (sedentary/lightly_active/moderately_active/very_active/super_active): ").lower()

# Calculate BMR
bmr = calculate_bmr(weight, height, age, gender)

# Calculate daily calorie needs
daily_calories = calculate_calories(bmr, activity_level)

# Display the result
print(f"Your estimated daily calorie needs are: {daily_calories:.2f} calories")
