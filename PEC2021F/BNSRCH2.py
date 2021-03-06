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
def upper_bound(l, r, x):
    
    while l < r-1:
        mid = (l+r)//2
        if find_pos(mid)==x:
            l = mid
        else:
            r = mid
    if find_pos(r)==x:
        return r
    else:
        return l

def lower_bound(l, r, x):
    while l < r-1:
        mid = (l+r)//2
        if find_pos(mid)==x:
            r = mid
        else:
            l = mid
    if find_pos(l)==x:
        return l
    else:
        return r
def count(n, x):
    global cnt
    l = 0
    r = n-1
    
    mid = (l+r)//2
    val = find_pos(mid)
    while l<=r:
        if val == x:
            break
        elif val>x:
            r = mid-1
        else:
            l = mid+1
        mid = (l+r)//2
        val = find_pos(mid)
    
    if val !=x:
        return 0    
    
    lowerLimit = lower_bound(l, mid, x)
    

    upperLimit = upper_bound(mid, r, x)
    
    return upperLimit-lowerLimit+1
# ----------------- Do not modify anything below this line -----------------------
 
n = int(input())
x = int(input())
 
print('2 ' + str(count(n, x)))
