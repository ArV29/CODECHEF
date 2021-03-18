length = int(input())

array = list(map(int, input().split()))

i = length -1
while i >= 0:
    print(array[i], end=" ")
    i -= 1
