from Crypto.Util.number import getPrime
from functools import lru_cache
import numpy as np 
import sys 

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

def rsa_encrypt_message(m, e, n):
    blocks = [int(x) for x in str(m)]
    c = []
    for block in blocks:
        c.append(encrypt_block(block, e, n))
    return c

def rsa_decrypt_message(c, d, n):
    blocks = [int(x) for x in c]
    m = []
    for block in blocks:
        m.append(decrypt_block(block, d, n))
    return m





def main():
    p, q = gen_p_q()
    n = gen_n(p, q)
    phi = gen_phi(p, q)
    e = gen_e(phi)
    d = gen_d(e, phi)
    m = int.from_bytes(b'boom', 'big')
    print(m)
    c = rsa_encrypt_message(m, e, n)
    print(c)
    m2 = rsa_decrypt_message(c, d, n)
    print(m2)
    m2 = [str(x) for x in m2]
    m2 = ''.join(m2)
    m2 = int(m2)
    m2 = m2.to_bytes((m2.bit_length() + 7) // 8, 'big').decode('utf-8')
    print(m2)
    # b = m2.to_bytes(, 'big')
    # b = b.decode('utf-8')
    # print(b)
    




if __name__ == '__main__':
    main()


    

