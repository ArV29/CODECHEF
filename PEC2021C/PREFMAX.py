print(2)
n = int(input())
arr = []
ans = 1
max = int(input())
for i in range(n-1):
    x = int(input())
    if x>max:
        ans+=1
        max = x
    
print(ans)