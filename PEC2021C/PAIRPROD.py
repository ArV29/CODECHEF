n = int(input())
arr =[]
print(2)
sum = int(input())
masterSum = 0
for i in range(n-1):
    x = int(input())
    masterSum = masterSum + x*(sum)
    sum+=x
    


print(masterSum)