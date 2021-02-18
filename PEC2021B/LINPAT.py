#Linear pattern Problem Code: LINPAT

n = int(input())

series1 = 10

series2 = 2

for i in range(n):
    if i % 2 == 0:
        print(series1, end=" ")
        series1 += 10
    else:
        print(series2, end=" ")
        series2 += 2
