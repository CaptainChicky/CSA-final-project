from math import sqrt
import random
from random import randint as rand

# standard gcd function
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# mod inverse for d
def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return -1
    else:
        return pow(a, -1, m)

# O(n log log n) complexity with  Sieve of Eratosthenes
def isprime(n):
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]

# initialize p q
p = 1
q = 1

# generate primes function
def generate_prime(bits):
    while True:
        # Generate a random odd number with the specified number of bits
        candidate = random.getrandbits(bits)
        # Ensure the number has the correct bit length and is odd
        candidate |= (1 << bits - 1) | 1  
        
        if isprime(candidate):
            return candidate

# generates the actual 2 pairs of keys
def generate_keypair(keysize):

    if keysize < 8:
        raise ValueError("The key size is too small to generate two distinct prime numbers.")


    # Generate two distinct prime numbers with the specified key size
    # i am doing //2 so that p and q values have similar bit-length.
    # this will generate an n value that's hard to factorize into p and q
    p = generate_prime(keysize // 2)
    q = generate_prime(keysize // 2)

    # also loop until they are distinct
    while p == q:
        p = generate_prime(keysize // 2)
        q = generate_prime(keysize // 2)

    # rest of the stuff needed for rsa
    n = p * q
    phi = (p - 1) * (q - 1)

    # generate a satisfactory e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # generates the d value
    d = mod_inverse(e, phi)

    # loop until they are distinct, since e may be bad
    while (n, e) == (n, d):
        # regenerate a satisfactory e
        e = random.randint(2, phi - 1)
        while gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        # regenerates the d value
        d = mod_inverse(e, phi)
    
    # (n, e) public key and (n, d) private key
    return ((n, e), (n, d))

def encrypt(msg_plaintext, package): # plain is converted into a Unicode code point list
    # unpack key value pair
    n, e = package
    # ord(c) converts the character c to its corresponding Unicode code point.
    # pow(ord(c), e, n) raises the Unicode code point to the power of e modulo n. 
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext # this is a list

def decrypt(msg_ciphertext, package): # ciper is a list
    n, d = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))