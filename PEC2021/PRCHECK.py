number = int(input())
if number == 1:
    print(0)
    exit()
counter = 2
for counter in range(2, int(number**0.5)+1):
    if number % counter == 0:
        print(0)
        exit()
print(1)
