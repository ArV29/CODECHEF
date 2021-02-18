length = int(input())
length -= 1
array = list(map(int, input().split()))
while length >= 0:
    print(array[length], end=" ")
length -= 1
