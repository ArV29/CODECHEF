x, y = input().split()
x = int(x)
y = int(y)
if x % 2 == 0:
    x += 1
while x <= y:
    print(x, end=" ")
    x += 2
