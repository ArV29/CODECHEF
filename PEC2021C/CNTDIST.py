print(2)

n = int(input())

dic = {}

cnt = 0 
for i in range(n):
    x = (input())
    if x in dic:
        continue
    else:
        cnt+=1
        dic[x] = True

print(cnt)