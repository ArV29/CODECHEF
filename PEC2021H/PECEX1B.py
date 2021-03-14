t = int(input())

for t in range(t):
    n = int(input())

    squares = []
    for i in range(1, (int(n**0.5)+1)):
        squares.append(i**2)
    pairs = []
    donePairs = []
    for i in range(len(squares)):

        if (n-squares[i]) in squares:
            pair = {int(squares[i]**0.5), int((n-squares[i])**0.5)}
            if not pair in pairs:
                pairs.append(pair)
                donePairs.append(
                    [int(squares[i]**0.5), int((n-squares[i])**0.5)])

    if len(donePairs) < 2:
        print("-1 -1 -1 -1")
    else:
        print(*donePairs[len(donePairs)-1], *donePairs[len(donePairs)-2])
