def calculateAreaOfCircle(radius_string):

    radius_string = input("please enter the radius of the circle")

    radius_float = float(radius_string)

    compute_circle_area = (radius_float**2)*3.14159265

    print(compute_circle_area)

calculateAreaOfCircle('radius_string')




def caculateMpg(driven_miles_string,gallons_used_string):
    driven_miles_string = input("Please enter the driven miles")
    gallons_used_string = input("Please enter the used gallons")

    driven_miles_float = float(driven_miles_string)
    gallons_used_float = float(gallons_used_string)

    caculateMpg = driven_miles_float / gallons_used_float
    print(caculateMpg)

caculateMpg('driven_miles_string','gallons_used_string')






def convertFahrenheitToCelsius(fahrenheit_degrees_string):
    fahrenheit_degrees_string = input("Please enter the fahrenheit degrees")

    fahrenheit_degrees_float = float(fahrenheit_degrees_string)

    celsius_degrees_float = float((fahrenheit_degrees_float - 32) * 5 / 9)

    print(celsius_degrees_float)

convertFahrenheitToCelsius('fahrenheit_degrees_string')




def DistanceBetweenPoints(pointX_string,pointX1_string,pointY_string,pointY1_string):
    pointX_string = input('Please enter the point X number')
    pointX1_string = input('Please enter the point X1 number')
    pointY_string = input('Please enter the point Y number')
    pointY1_string = input('Please enter the point Y1 number')

    pointX_int = int(pointX_string)
    pointX1_int = int(pointX1_string)
    pointY_int = int(pointY_string)
    pointY1_int = int(pointY1_string)

    distance_between_X_and_X1 = pointX1_int - pointX_int
    distance_between_Y_and_Y1 = pointY1_int - pointY_int
    DistanceBetweenPoints = (distance_between_X_and_X1,distance_between_Y_and_Y1)

    print(DistanceBetweenPoints)


DistanceBetweenPoints('pointX_int','pointX1_int','pointY_int','pointY1_int')