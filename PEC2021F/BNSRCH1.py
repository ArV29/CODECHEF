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
    low = 1
    high = 1000000000-1



    
    while low <high-1:
        mid = (low+high)//2
        if run_program(mid):
            low = mid
        else:
            high = mid
        
       



    if run_program(high):
        return high
    else:
        return low
 
# ------------------- Do not touch anything below this line -------------------------------------
print("2 " + str(find_memory_limit()))
# cook your dish here
