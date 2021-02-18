#Alternative Square Pattern Problem Code: SQALPAT

n = int(input())

i = 1
while i <= n:
    for counter in range((i-1)*5+1, 5*i+1):
        print(counter, end=" ")
    i += 1
    print()
    for counter in reversed(range((i-1)*5+1, 5*i+1)):
        print(counter, end=" ")
    print()
    i += 1
