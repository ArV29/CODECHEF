t = int(input())

for t in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxLen = 0
    for i in range(n):
        for ii in range(i+1, n+1):
            a = A[i:ii]
            a.sort()
            b = B[i:ii]
            b.sort()
            if a == b and ii-i > maxLen:
                maxLen = ii - i
    print(maxLen)
