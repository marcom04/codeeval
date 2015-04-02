# https://www.codeeval.com/open_challenges/4/

import sys

def generate_prime():  
    # For each composite number encountered, i, 
    # prime_divisors[i] is a list of primes that divide i
    prime_divisors = {}
    current = 2  

    while True:
        if current not in prime_divisors:
            # current is prime
            yield current        
            prime_divisors[current * current] = [current]
        else:
            # current is composite
            for p in prime_divisors[current]:
                prime_divisors.setdefault(p + current, []).append(p)
            del prime_divisors[current]
        
        current += 1


gen = generate_prime()
sum = 0

for i in range(1000):
    sum += gen.next()
    
print sum    
