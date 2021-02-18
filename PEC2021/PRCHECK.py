number = int(input())
if number == 1:
    print(0)
    exit()
counter = 2
while counter <= number**0.5:
    if number % counter == 0:
        print(0)
        exit()
counter += 1
print(1)
