import math
n = int(input())

dic = {}

amount = 0

for i in range(n):
    
    action = input()
    name = input()
    time = int(input())
    
    if action == "entry":
        dic[name]=time
    else:
        
        time = time - dic[name]
        time = time/60
        time = math.ceil(time)
        if time >1:
            amount+=(60 + (time-1)*30)
        else:
            amount+=60
    

print(amount)
        
        