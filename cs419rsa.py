import sympy
from functools import lru_cache
from random import randint
import sys

def rsa_encrypt(m, e, n):
    """
    This function encrypts a message
    This function encrypts a message
    @param m: message of type int 
    @param e: public exponent 
    @param n: its n
    """
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    """
    This function decrypts a message
    @param c: ciphertext of type int
    @param d: private exponent
    @param n: its n
    @return: plaintext of type int
    """
    return pow(c, d, n)

def rsa_sign(m, d, n):
    """
    This function signs a message
    @param m: message of type int
    @param d: private exponent
    @param n: its n
    """
    return rsa_decrypt(m, d, n)

def rsa_verify(s, e, n):
    """
    This function verifies a signature
    @param s: signature of type int
    @param e: public exponent
    @param n: its n
    """
    return rsa_encrypt(s, e, n)




def rsa_keygen(p, q):
    """
    This function generates a public and private key for RSA
    @param p: prime number that the user selects or is generated randomly
    @param q: prime number that the user selects or is generated randomly
    @return: a tuple of (n, e, d)
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = modinv(e, phi)
    return (n, e, d)

def modinv(a, m):
    """
    This function finds the modular inverse of a number and is euclidian extended
    @param a: integer
    @param m: modulus
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None



def rsa_encrypt_message(data, e, n):
    """
    This function encrypts a file and writes it to a new file and can be modified to 
    work with socket messages.
    @param data: data to encrypt
    @param e: public exponent
    @param n: its n
    @return: encrypted data
    """
    data = [ord(c) for c in data]
    print(data)
    data = [rsa_encrypt(c, e, n) for c in data]
    print(data)
    data = [chr(c) for c in data]
    data = ''.join(data)
    return data

def rsa_decrypt_message(data, d, n):
    """
    This function decrypts a file and writes it to a new file and can be modified to 
    work with socket messages.
    @param data: data to decrypt
    @param d: private exponent
    @param n: its n
    @return: decrypted data
    """
    data = [ord(c) for c in data]
    data = [rsa_decrypt(c, d, n) for c in data]
    print(data)
    data = [chr(c) for c in data]
    data = ''.join(data)
    return data

def generate_p_q():
    """
    This function generates a public and private key for RSA
    @return: a tuple of (n, e, d)
    """
    p = nth_prime(randint(1000, 2000))
    q = nth_prime(randint(1000, 2000))
    # p = sympy.randprime(1000000, 100000000000)
    # q = sympy.randprime(1000000, 100000000000)
    return p, q


'''[9768054, 8135966, 20797583, 62401383, 113287187]'''
''' '''
@lru_cache(maxsize=None)
def isPrime(n, i=2):
 
    # Base cases
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
 
    # Check for next divisor
    return isPrime(n, i + 1)



def nth_prime(n):
    """
    This function finds the nth prime number
    @param n: nth prime number
    @return: nth prime number
    """
    i = 2
    while n > 0:
        if isPrime(i):
            n -= 1
        i += 1
    return i - 1



if __name__ == '__main__':
    # p, q = generate_p_q()
    p = 11087
    q = 11783
    n, e, d = rsa_keygen(p, q)
    print('p:', p)
    print('q:', q)
    print('n:', n)
    print('e:', e)
    print('d:', d)
    file = input('File: ')
    data = rsa_encrypt_message(file, e, n)
    data2 = rsa_decrypt_message(list(data), d, n)
    print(data)
    print(data2)
    # with open(file, 'w') as f:
    #     f.write(data)
    # data = rsa_decrypt_file(file, d, n)
    # with open(file, 'w') as f:
    #     f.write(data)