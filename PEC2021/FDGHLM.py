arr = list(map(int, input().split(" ")))
x = arr[0]
y = arr[1]
X = x
Y = y
if x > y:
    x, y = y, x
while x % y != 0:
    temp = y
    y = x
    x = temp % x
hcf = x
lcm = int((X*Y)/hcf)
print(hcf, lcm)
