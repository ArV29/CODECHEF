def isPrime(n):
    if (n == 1) or (n == 0):
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


primes = set()
notPrimes = set()
check = set()
t = int(input())
for t in range(t):
    n = int(input())
    N = n
    mid = n//2
    while mid > 0:
        if mid in check:
            if mid in primes:
                if (n-mid) in check:
                    if (n-mid) in primes:
                        print(mid, (n - mid))
                        break
                else:
                    check.add(n-mid)
                    if isPrime(n-mid):
                        primes.add(n-mid)
                        print(mid, (n - mid))
                        break
                    else:
                        notPrimes.add(n-mid)
        else:
            check.add(mid)
            if isPrime(mid):
                primes.add(mid)
                if (n-mid) in check:
                    if (n-mid) in primes:
                        print(mid, (n - mid))
                        break
                else:
                    check.add(n-mid)
                    if isPrime(n-mid):
                        primes.add(n-mid)
                        print(mid, (n - mid))
                        break
                    else:
                        notPrimes.add(n-mid)
            else:
                notPrimes.add(mid)

        mid -= 1

    if mid == 0:
        print(-1, -1)
