import time
from Crypto.Util.number import getPrime, inverse

e = 65537
m = 476921883457909
def generate_keypair(p, q):  
    phi = (p - 1) * (q - 1)
    while True:
        public = getPrime(1024)
        if e < phi and phi % e != 0:
            break
    
    private = inverse(public, phi)
    if((public * private) % phi != 1):
        print("Error generating keys")
    
    return public, private

def encrypt(pk,n, plaintext):
    
    cipher = pow(plaintext, pk, n)
    
    return cipher

def decrypt(pk,n, ciphertext):
    start = time.time()
    plain = pow(ciphertext, pk, n)  
    print("decrypt took:",time.time() - start)
    return plain

def chineseRemainderTheorem(c, d, p, q):
    start = time.time()
    dp = d % (p-1)
    dq = d % (q-1)
    qInv = inverse(q,p)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (qInv * (m1 - m2)) % p
    m = m2 + h*q
    print("CRT took:",time.time() - start)
    return m

def encrypt2(pk,n, plaintext):
    cipher = pow(int(plaintext), pk, n) 
    return cipher

def main():
    #generate two random 1024 bit prime numbers

    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    #generate the public and private keys
    public, private = generate_keypair(p, q)
    encrypted = encrypt(public,n, m)
    
    
    decrypted = decrypt(private,n, encrypted)
    decryptedcrt = chineseRemainderTheorem(encrypted, private, p, q)
    
    print("decrypted:",decrypted)

main()