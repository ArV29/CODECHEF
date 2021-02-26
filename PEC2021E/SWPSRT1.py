n = int(input())

arr = list(map(int, input().split()))

counter = 0
swapList = []
for i in range(n):
    min = arr[i]
    index = i
    for ii in range(i+1, n):
        if arr[ii] < min:
            index = ii
            min = arr[ii]
    if arr[index] < arr[i]:
        counter += 1
        arr[i], arr[index] = arr[index], arr[i]
        swapList.append([i, index])

print(counter)

for swap in swapList:
    print(*swap)
