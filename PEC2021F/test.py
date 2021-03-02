def choose_pivot(arr):
    pivots = {}

    for i in range(len(arr)):
        if arr[i][0] in pivots:
            continue
        pivots[arr[i][0]] = i

   
    pivot = list(pivots.values())
    return(sorted(pivot))


print(choose_pivot([(0, 0), (2, 0), (2, 1), (-1, 0), (-1, 1), (0, 1)]))
