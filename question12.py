user_enter_fahrenheit_degrees_string = input("Please enter the fahrenheit degrees")

user_enter_fahrenheit_degrees_float = float(user_enter_fahrenheit_degrees_string) 

celsius_degrees_float = float((user_enter_fahrenheit_degrees_float-32)*(5/9))

print(celsius_degrees_float)