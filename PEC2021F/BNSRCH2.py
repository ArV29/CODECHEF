def find_pos(X):
    global arr
    global cnt
    cnt +=1
    return arr[X]




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

    
                
            
                
        
def create_arr():
    global arr
    for i in range(100000//4):
        arr.append(6)
    arr.append(7)
    
        
    for i in range(100000//2):
        arr.append(8)
    
    
    


def main():
    global arr
    global cnt
    arr = []
    create_arr()
    cnt = 0
    print(count(len(arr), 7), "CNT: ", cnt)

    


main()
