t = int(input())

for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    if b==a:
        print("yes")
    else:
        print("no")