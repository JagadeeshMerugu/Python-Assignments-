k = int(input())
rooms = list(map(int, input().split()))

room_count = {}

for room in rooms:
    if room in room_count:
        room_count[room] += 1
    else:
        room_count[room] = 1

for room, count in room_count.items():
    if count != k:
        print(room)
        break
