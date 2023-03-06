n = int(input("the number of elements in the set: "))
s = set(map(int, input().split()))

for _ in range(int(input())):
    name, *args = input().split()
    getattr(s, name)(*map(int, args))

print(sum(s))
