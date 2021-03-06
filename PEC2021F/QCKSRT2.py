# you can use this less than comparator operator in the choose_pivot, if you would like
# keep in mind that this is the comparator used in the quick sort implementation given
def lessthan(x, y):
    return x[0] < y[0]

# complete this function
# the return value is wrong, you are to complete this function so that the return value is correct
# arr is a list of tuples where each tuple contains the pair (x, y)


def choose_pivot(arr):
    indices = {}

    for i in range(len(arr)):
        if arr[i][0] in indices:
            continue
        indices[arr[i][0]] = i

    index = list(indices.values())
    index = sorted(index)
    return(index)


# ---------------------------- Do not modify code below this line ------------------------------------
n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))

candidates = choose_pivot(arr)

print(len(candidates))
print(*candidates)
