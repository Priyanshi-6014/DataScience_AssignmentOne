import math

def area_of_circle(radiusOfCircle1, radiusOfCircle2):
    radius1 = int(radiusOfCircle1)                # converting input to int
    radius2 = int(radiusOfCircle2)

    areaOfCircle1 = math.pi * radius1**2
    areaOfCircle2 = math.pi * radius2**2
    max_area = max(areaOfCircle1, areaOfCircle2)
    min_area = min(areaOfCircle1,areaOfCircle2)
    proportion = int((min_area/max_area)*100)     #to find proportion
    print(f'The percentage  is {proportion}%')



area_of_circle(10,10)