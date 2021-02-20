def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        
        subset= [[]]
        for i in range(1, n+1):
            
            for ii in range(0, 2**(i-1)):
                subset.append(subset[ii]+[i])
                print(*subset[len(subset)-1])
        print()



main()
