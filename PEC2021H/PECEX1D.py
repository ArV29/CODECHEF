t = int(input())


def move(x, n):
    global N
    if x == 1:
        count = 0
        for i in range(-3, 4):
            if n-i == 0:
                count += 1
        return count

    count = 0
    for i in range(-3, 4):
        if 0 <= n-i <= N:

            count += move(x-1, n-i)
    return count


for t in range(t):
    global N
    N, x = map(int, input().split())
    if x == 0:
        if N == 0:
            print(1)
        else:
            print(0)
        continue
    count = move(x, N)

    print(count)
