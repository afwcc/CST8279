def convertFahrenheitToCelsius(fahrenheit_degrees_string):
    fahrenheit_degrees_string = input("Please enter the fahrenheit degrees")

    fahrenheit_degrees_float = float(fahrenheit_degrees_string)

    celsius_degrees_float = float((fahrenheit_degrees_float - 32) * 5 / 9)

    print(celsius_degrees_float)

convertFahrenheitToCelsius('fahrenheit_degrees_string')