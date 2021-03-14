t = int(input())

for t in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[2])
