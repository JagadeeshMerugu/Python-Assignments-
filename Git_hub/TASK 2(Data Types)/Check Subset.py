


t = int(input())

for i in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    
    m = int(input())
    b = set(map(int, input().split()))
    
    if a.issubset(b):
        print(True)
    else:
        print(False)
