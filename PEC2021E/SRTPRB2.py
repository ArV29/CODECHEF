def profitableMatches(arr):
    if len(arr) == 2:

        if arr[0] != arr[1]:
            return 1
        else:
            return 0

    mid = len(arr)//2

    leftProfitableMatches = profitableMatches(arr[:mid])
    rightProfitableMatches = profitableMatches(arr[mid:])

    matchesA = set(arr[:mid])
    matchesB = set(arr[mid:])

    if (matchesA & matchesB):
        return leftProfitableMatches+rightProfitableMatches
    else:
        return leftProfitableMatches+rightProfitableMatches+1


n = int(input())

arr = list(map(int, input().split()))


print(profitableMatches(arr))
