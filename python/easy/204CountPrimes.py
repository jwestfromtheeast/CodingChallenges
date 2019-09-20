# Leetcode 204
class Solution:
    # Use sieve of Eratosthenes
    # Complexity: Time O() Space O()
    def primes(self, n: int) -> int:
        sieve = [True for i in range(n)]
        sieve[0], sieve[1] = False, False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i] == True:
                for j in range(i * i, n, i):
                    sieve[j] = False
        return sieve
            
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        sieve = self.primes(n)
        count = 0
        for i in range(len(sieve)):
            if sieve[i]:
                count +=1
        return count