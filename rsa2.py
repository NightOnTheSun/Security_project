from Crypto.Util.number import getPrime
from functools import lru_cache
import numpy as np 

def gen_p_q():
    return getPrime(512), getPrime(512)

def gen_n(p, q):
    return p * q

def gen_phi(p, q):
    return (p - 1) * (q - 1)

def gen_e(phi):
    e = 3
    while e < phi:
        if gcd_euclid(e, phi) == 1:
            return e
        e += 1

@lru_cache(maxsize=None) 
def gcd_euclid(a, b):
    if b == 0:
        return a
    return gcd_euclid(b, a % b)

def gcd_euclid_extended(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = gcd_euclid_extended(b, a % b)
    return y, x - (a // b) * y, d

def mod_inv_euclid_extended(a, m):
    x, y, d = gcd_euclid_extended(a, m)
    if d == 1:
        return x % m
    return None

def gen_d(e, phi):
    return mod_inv_euclid_extended(e, phi)

def encrypt_block(m, e, n):
    return pow(m, e, n)

def decrypt_block(c, d, n):
    return pow(c, d, n)

def encrypt(m, e, n):
    print(m.to_bytes(n.bit_length() // 8, 'big').hex())
    blocks = [encrypt_block(m, e, n) for m in m.to_bytes(n.bit_length() // 8, 'big')]
    # print(blocks)
    return bytes(blocks)

def decrypt(c, d, n):
    blocks = [decrypt_block(c, d, n) for c in c.to_bytes(n.bit_length() // 8, 'big')]
    return bytes(blocks)

def main():
    p, q = gen_p_q()
    n = gen_n(p, q)
    phi = gen_phi(p, q)
    e = gen_e(phi)
    d = gen_d(e, phi)
    m = int.from_bytes(b'poof', 'big')
    c = encrypt(m, e, n)
    # print(c)
    m2 = decrypt(c, d, n)
    print(m2)




if __name__ == '__main__':
    main()


    

