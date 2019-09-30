def caculateMpg(driven_miles_string,gallons_used_string):
    driven_miles_string = input("Please enter the driven miles")
    gallons_used_string = input("Please enter the used gallons")

    driven_miles_float = float(driven_miles_string)
    gallons_used_float = float(gallons_used_string)

    caculateMpg = driven_miles_float / gallons_used_float
    print(caculateMpg)

caculateMpg('driven_miles_string','gallons_used_string')