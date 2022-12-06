def isPrime(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True
    
def solution(i):
    primes = ''
    for num in range(2,22000):
        if len(primes) < 10000:
            if isPrime(num):
                primes += str(num)
        else:
            break
    n = i+5
    #print(primes)
    return primes[i:n]