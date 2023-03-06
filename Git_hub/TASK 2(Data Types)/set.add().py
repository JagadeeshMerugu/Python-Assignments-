
number = int(input("The total number of country:"))
lst = []
for i in range(number):
    enter = input("Name of the country:")
    lst.append(enter)
    
resultado = len(set(lst))

print(resultado)
