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