n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

result = len(english.symmetric_difference(french))

print(result)
