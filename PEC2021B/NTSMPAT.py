#Not Simple Pattern Problem Code: NTSMPAT
 
 
n = int(input())
 
i = 1
 
while i<=n:
    midVal = 2*i-1
    j=i
    while j <=midVal:
        print(j, end = " ")
        j+=1
    j-=2
    while j>=i:
        print(j, end=" ")
        j-=1
    print()
    i+=1