x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
z = int(input("Enter z value:"))
n = int(input("Enter n value:"))
for i in range(4): 
        result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z          +1) if i+j+k!=n]
print(result)