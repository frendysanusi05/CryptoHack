'''
Fermat's little theorem

if p is prime, for every integer a:
	pow(a, p) = a mod p

if p is prime and a is an integer coprime with p:
	pow(a, p-1) = 1 mod p

given a = 273246787654, p = 65537

check if a and p are coprime
'''

from math import gcd

a = 273246787654
p = 65537

assert(gcd(a,p) == 1)

# because the gcd is 1, then a^(p-1) mod p = 1