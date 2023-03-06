setA = set(input().split())
n = int(input())
is_strict_superset = True
for _ in range(n):
    setB = set(input().split())
    if not setB.issubset(setA) or setB == setA:
        is_strict_superset = False
        break
print(is_strict_superset)
