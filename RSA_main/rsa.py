import random

def gcd(a, b):
    """Standard GCD function."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Modular inverse for computing d."""
    if gcd(a, m) != 1:
        return -1
    else:
        return pow(a, -1, m)

def isprime(n):
    """Primality test using Sieve of Eratosthenes. O(n log log n) complexity."""
    if n < 2:
        return False
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve[n]

def generate_prime(bits):
    """Generate a prime number with the specified bit length."""
    while True:
        candidate = random.getrandbits(bits)
        # Ensure the number has the correct bit length and is odd
        candidate |= (1 << bits - 1) | 1
        if isprime(candidate):
            return candidate

def generate_keypair(keysize):
    """Generate RSA public and private key pair.
    
    Returns ((n, e), (n, d)) where (n, e) is the public key and (n, d) is the private key.
    Using keysize // 2 for p and q so they have similar bit-length,
    producing an n that's hard to factorize.
    """
    if keysize < 8:
        raise ValueError("The key size is too small to generate two distinct prime numbers.")

    p = generate_prime(keysize // 2)
    q = generate_prime(keysize // 2)
    while p == q:
        q = generate_prime(keysize // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Generate e such that gcd(e, phi) == 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    # Ensure e != d
    while e == d:
        e = random.randint(2, phi - 1)
        while gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        d = mod_inverse(e, phi)

    return ((n, e), (n, d))

def encrypt(msg_plaintext, package):
    """Encrypt plaintext string using RSA public key.
    
    Each character is converted to its Unicode code point,
    then raised to the power of e modulo n.
    Returns a list of encrypted integers.
    """
    n, e = package
    return [pow(ord(c), e, n) for c in msg_plaintext]

def decrypt(msg_ciphertext, package):
    """Decrypt RSA ciphertext back to plaintext string.
    
    Each integer is decrypted and converted back to a character.
    """
    n, d = package
    return ''.join(chr(pow(c, d, n)) for c in msg_ciphertext)