letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
keys = []


for a in letters:
    if a == "a":
        continue
    for b in letters:
        if b=="b" or b==a:
            continue
        
        for c in letters:
            if c =="c" or c==a or c == b:
                continue
            
            for d in letters:
                if d == "d" or d == a or d == b or d ==c:
                    continue
                for e in letters:
                    if e =="e" or e == a or e ==b or e == c or e==d:
                        continue
                    for f in letters:
                        if f=="f" or f ==a or f == b or f == c or f ==d or f ==e :
                            continue
                        for g in letters:
                            if g =="g" or g ==a or g == b or g ==c or g == d or g ==e or g == f:
                                continue
                            for h in letters:
                                if h == "h" or h == a or h == b or h == c or h == d or h == e or h == f or h ==g :
                                    continue
                                keys.append({"a": a, "b": b, "c": c, "d": d, "e": e, "f":  f, "g": g, "h": h})
    


w = int(input())
letter= set(letters)
words = set()

for i in range(w):
    word = input()
    words.add(word)


secretMessage = input().split()
i = 0
j = 0
possibleKey = [False, None]
while i < len(secretMessage):
    
    
    while j<len(keys):
        secretWord = secretMessage[i]
        decryptedWord  = ""
        key = keys[j]
        for char in secretWord:
            if not char in letter:
                decryptedWord+=char    
            else:
                decryptedWord += key[char]
        if decryptedWord in words:
            
            i+=1
            possibleKey[0] = True
            possibleKey[1] = j
            break
        else:
            
            if possibleKey[0]:
                possibleKey[0] = False
                possibleKey[1] = None
                i = 0
            j+=1
    

decreypt = []
for secretWord in secretMessage:
    decryptedWord = ""
    for char in secretWord:
        if not char in letters:
            decryptedWord += char
        else:
            decryptedWord += keys[possibleKey[1]][char]
    decreypt.append(decryptedWord)

print(*decreypt)
            


