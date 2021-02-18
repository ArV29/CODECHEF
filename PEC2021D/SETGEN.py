def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        
        subset= []
        for ii in range(1, n+1):
            subset.append(ii)
            print(ii)
            for iii in range(0, 2**(ii-1)-1):
                if type(subset[iii]) == int:
                    subset.append([subset[iii]]+ [ii])
                else:
                    subset.append(subset[iii]+[ii])
                print(*subset[len(subset)-1])
        print()



main()
