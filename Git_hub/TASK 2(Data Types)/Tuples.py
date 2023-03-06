n = int(input())
integer_list = tuple(map(int, input().split()))
hash_value = hash(integer_list)
print(hash_value)
