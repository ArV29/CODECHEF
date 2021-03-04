




import sys
 
def find_pos(x):
    print('1 ' + str(x))
    sys.stdout.flush()
    t = int(input())
    return t
# ----------------- Do not modify anything above this line -----------------------
# Complete this function count(n, x), this returns 0 always and hence is wrong, it should return the number of occurrences of x in Chef's array
# You can use the function find_pos(x) to find the value of the element at position x (0 indexed)
# If the index is invalid or you use more than 40 queries to obtain the value, you will receive Wrong Answer
# Chef's array size is not more than 10 ** 5
def upper_bound(low, high, X):
    
    while low < high-1:
        middle = (low+high)//2
        if find_pos(middle)==X:
            low = middle
        else:
            high = middle
    if find_pos(high)==X:
        return high
    else:
        return low

def lower_bound(low, high, X):
    while low < high-1:
        middle = (low+high)//2
        if find_pos(middle)==X:
            high = middle
        else:
            low = middle
    if find_pos(low)==X:
        return low
    else:
        return high
def count(n, X):
    global cnt
    low = 0
    high = n-1
    
    middle = (low+high)//2
    val = find_pos(middle)
    while low<=high:
        if val == X:
            break
        elif val>X:
            high = middle-1
        else:
            low = middle+1
        middle = (low+high)//2
        val = find_pos(middle)
    
    if val !=X:
        print("value not found")
        return 0
    
    lowerLimit = lower_bound(low, middle, X)
    

    upperLimit = upper_bound(middle, high, X)
    
    return upperLimit-lowerLimit+1

    
# ----------------- Do not modify anything below this line -----------------------
 
n = int(input())
x = int(input())
 
print('2 ' + str(count(n, x)))
