number=int(input("Enter a number: "))

if number % 2 ==1 :
    print("Weird")
elif number in range (2,6):
    print("Not Weird")
elif number in range(6,21):
    print("Weird")
else:
    print("Not Weird")