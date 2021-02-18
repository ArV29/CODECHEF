length, key = input().split()
key = int(key)
array = list(map(int, input().split()))
if key in array:
    print(1)
else:
    print(-1)
