#Good Number Or Not Problem Code: ISGOODNM
n = int(input())

sum = 1

for i in range(2, int(n**0.5)):
    if n % i == 0:
        sum += i
        sum += (n//i)
    if sum >= n:
        break
if sum == n:
    print("YES")
else:
    print("NO")
