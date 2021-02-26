

def checkKey(words, secretMessage, key):
    for word in secretMessage:
        decryptedWord = decrypt(word, key)
        if not decryptedWord in words:
            return False
    return True




def decrypt(word, key):
    decryptedWord = ""
    for letter in word:
        decryptedWord += key.get(letter, letter)
    return decryptedWord


def decryptMessage(secretMessage, key):
    decryptedMessage = []
    for word in secretMessage:
        decryptedMessage.append(decrypt(word, key))
    return decryptedMessage

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
keys = []





w = int(input())
letter= set(letters)
words = set()

for i in range(w):
    word = input()
    words.add(word)


secretMessage = input().split()
for a in letters:
    if a == "a":
        continue
    for b in letters:
        if b == "b" or b == a:
            continue

        for c in letters:
            if c == "c" or c == a or c == b:
                continue

            for d in letters:
                if d == "d" or d == a or d == b or d == c:
                    continue
                for e in letters:
                    if e == "e" or e == a or e == b or e == c or e == d:
                        continue
                    for f in letters:
                        if f == "f" or f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in letters:
                            if g == "g" or g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in letters:
                                if h == "h" or h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                key = {"a": a, "b": b, "c": c, "d": d,
                                       "e": e, "f": f, "g": g, "h": h}
                                if checkKey(words, secretMessage, key):
                                    print(*decryptMessage(secretMessage, key))
                                    exit()



