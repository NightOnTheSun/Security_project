from sympy import randprime


p = 0
q = 0
r = 257
while r > 256:
    
    p = randprime(2,250)
    
    q = randprime(2,250)
    if p == q:
        
        p = randprime(2,250)
        
        q = randprime(2,250)
    
    r = p * q


e = (p-1)*(q-1)


pub_key = randprime(2,e)
print("Public Key: ",pub_key)

d = 0
while d < 1000000000:
    if (pub_key * d) % e == 1:
        break
    d = d+1
priv_key = d
print("Private Key: ",priv_key)
   
