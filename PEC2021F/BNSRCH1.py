import sys
 
def run_program(m):
    print('1 ' + str(m))
    sys.stdout.flush()
    r = int(input())
    if r == 0:
        return False
    elif r == 1:
        return True
    exit()
 
 
# ------------------- Do not touch anything above this line -------------------------------------
 
# complete the function below, use run_program(x) to determine if Chef's program can consume x bytes
# The result will be True if it can and False otherwise
# If you call the function run_program more than 31 times, you will get a wrong answer verdict
def find_memory_limit():
    l = 1
    r = 1000000000-1
    while l < r-1:
        mid = (l+r)//2
        if run_program(mid):
<<<<<<< HEAD
            low = mid
        else:
            high = mid



    if run_program(high):
        return high
    else:
        return low


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
=======
            l  = mid
        else:
            r = mid
    if run_program(r):
        return r
    else:
        return l
 
# ------------------- Do not touch anything below this line -------------------------------------
print("2 " + str(find_memory_limit()))
>>>>>>> 76559b57d8482c966d6b36dddcfb7cb2eb53f629
