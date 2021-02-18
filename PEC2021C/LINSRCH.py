n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    
arr= set(arr)

q = int(input())
print(1)

for i in range(q):
    number = int(input())
    if number in arr:
        print("yes")
    else:
        print("no")
