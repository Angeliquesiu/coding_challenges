# PRIME NUMBERS

# count number of prime numbers less than a non-negative number, n
# method: sieve of eratosthenes
# input: n = 10
# output : 4

def countPrimes(n):
    prime = [False, False] + [True] * (n - 2)

    i = 2
    while i * i < n:
        if prime[i]:
            j = i * i
            while j < n:
                prime[j] = False
                j += i
        i += 1
    return sum(prime)