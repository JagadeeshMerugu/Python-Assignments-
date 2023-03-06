from math import atan, degrees
AB = int(input("Enter AB value:"))
BC = int(input("Enter BC value:"))

angleC = atan(AB/BC)
print((round(degrees(angleC))),chr(176),sep='')

