class Solution:
    def countPrimes(self, n: int) -> int:
        if(n < 2):
            return 0
        primes = [True]*(n)
        primes[0] = False
        primes[1] = False
        p = 2
        res = 0
        while(p*p < n):
            if primes[p] == True:
                for i in range(p * 2, n, p):
                    primes[i] = False
            p+=1

        for i in primes:
            if i == True:
                res+=1
        return res