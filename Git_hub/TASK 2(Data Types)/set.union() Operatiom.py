a, A = (int(input("a number of students:")), set(map(int, input().split())))
b, B = (int(input("b number of students:")), set(map(int, input().split())))
print(len(A.union(B)))
