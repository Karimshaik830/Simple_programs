import math

# Solution class containing segmented sieve logic
class Solution:
    def segmentedSieve(self, a, b):
        # Find all primes up to sqrt(b)
        limit = int(math.sqrt(b)) + 1
        isPrime = [True] * (limit)
        isPrime[0] = isPrime[1] = False

        # Sieve of Eratosthenes
        for i in range(2, int(math.sqrt(limit)) + 1):
            if isPrime[i]:
                for j in range(i * i, limit, i):
                    isPrime[j] = False

        # Store small primes
        smallPrimes = [i for i in range(2, limit) if isPrime[i]]

        # Initialize range array
        isPrimeRange = [True] * (b - a + 1)

        # Mark non-primes in range [a, b]
        for p in smallPrimes:
            start = max(p * p, ((a + p - 1) // p) * p)
            for j in range(start, b + 1, p):
                isPrimeRange[j - a] = False

        # Store result
        result = []
        for i in range(len(isPrimeRange)):
            if isPrimeRange[i] and (i + a) > 1:
                result.append(i + a)

        return result

# Driver function
if __name__ == "__main__":
    a, b = 10, 30
    obj = Solution()
    primes = obj.segmentedSieve(a, b)
    print(primes)
