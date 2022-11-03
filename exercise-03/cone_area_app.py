from cone_area_lib import cone_area

radius = float(input('Radius: '))
height = float(input('Höhe: '))
print(f"Mantelfläche: {cone_area(radius, height)}")
