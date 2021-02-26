

n = int(input())

arr = list(map(int, input().split()))


def bubble(arr):
    swaps = 0
    swap = []
    n = len(arr)
    for i in range(n):
        SWAP = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swaps += 1
                swap.append(j)
                arr[j+1], arr[j] = arr[j], arr[j+1]
                SWAP = True
        if not SWAP:
            print(swaps)
            for s in swap:
                print(s, end=" ")
            return


bubble(arr)
