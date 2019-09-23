user_enter_number_driven_miles_string = input("Please enter the driven miles")
user_enter_number_gallons_used_string = input("Please enter the used gallons")

user_enter_number_driven_miles_float = float(user_enter_number_driven_miles_string)
user_enter_number_gallons_used_float = float(user_enter_number_gallons_used_string)

compute_MPG = user_enter_number_driven_miles_float/user_enter_number_gallons_used_float
print(compute_MPG)