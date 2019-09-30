def DistanceBetweenPoints(pointX_string,pointX1_string,pointY_string,pointY1_string):
    pointX_string = input('Please enter the point X number')
    pointX1_string = input('Please enter the point X1 number')
    pointY_string = input('Please enter the point Y number')
    pointY1_string = input('Please enter the point Y1 number')

    pointX_float = float(pointX_string)
    pointX1_float = float(pointX1_string)
    pointY_float = float(pointY_string)
    pointY1_float = float(pointY1_string)

    distance_between_X_and_X1 = pointX1_float - pointX_float
    distance_between_Y_and_Y1 = pointY1_float - pointY_float
    DistanceBetweenPoints = (distance_between_X_and_X1,distance_between_Y_and_Y1)

    print(DistanceBetweenPoints)


DistanceBetweenPoints('pointX_float','pointX1_float','pointY_float','pointY1_float')