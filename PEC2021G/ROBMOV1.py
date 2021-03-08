t = int(input())

for i in range(t):
    x, y, X, Y = list(map(int, input().split()))
    if x < X:
        moveX = 'E'
    if x > X:
        moveX = 'W'

    if y < Y:
        moveY = 'N'
    if y > Y:
        moveY = 'S'

    count = abs(X-x) + abs(Y-y)
    print(count)
    for i in range(abs(X-x)):
        print(moveX, end='')
    for i in range(abs(Y-y)):
        print(moveY, end='')
    print('')
