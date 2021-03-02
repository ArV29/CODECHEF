def run_program(x):
    global cnt
    global L
    
    cnt+=1
    return x>=L


def find_memory_limit():
    low = 1
    high = 1000000000-1



    
    while low < high-1:
        mid = (low+high)//2
        if run_program(mid):
            high = mid
        else:
            low = mid



    if run_program(low):
        return low
    else:
        return high


def main():
    global cnt
    cnt = 0
    global L
    for L in reversed(range(1, 1000000000)):
        calcL = find_memory_limit()
        if L == calcL and cnt<=31:
            print("For L:", L,"\n***** Success *****")
        else:
            print("Unsuccessfull at", L)
            print("Given L:", L, "\t\tCalculated L", calcL, "\t\tTries", cnt)
            break
        cnt = 0


main()
