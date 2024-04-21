import hashlib
import random

from Crypto.PublicKey import DSA



# Generate a random prime number
def generate_prime():
    # Your code to generate a prime number goes here
    pass

# Generate DSA parameters

def generator(p, q):
 for h in range(2, p - 1):
    g = pow(h, (p - 1) // q, p)
    if g > 1:
        return g


def generate_dsa_parameters():
    #generate p and q primes using Crypto.publickey.DSA
    key = DSA.generate(1024)
    p = key.p
    q = key.q
    # Choose an integer g such that g^q mod p = 1
  
    g = generator(p, q)
    return p, q, g

# Generate DSA key pair
def generate_dsa_key_pair():
    p, q, g = generate_dsa_parameters()

    # Choose a private key x
    x = random.randint(1, q)

    # Calculate the public key y
    y = pow(g, x, p)

    return (p, q, g), (x, y)

# Sign a message using DSA
def sign_message(message, x, public_key,k):
    p, q, g = public_key
    

    # Calculate the hash of the message using SHA-1
    
 # Calculate r
    r = pow(g, k, p) % q
 # Calculate s
    hash_message = int(hashlib.sha1(message.encode('utf-8')).hexdigest(), 16)
    k_inv = pow(k, -1, q)
    s = (k_inv * (hash_message + x * r)) % q
    return r, s
def verify_signature(message, signature, public_key,y):
    p, q, g = public_key
    
    r, s = signature

    # Calculate the hash of the message using SHA-1
    hash_value = int(hashlib.sha1(message.encode('utf-8')).hexdigest(), 16)

    # Calculate w = s^(-1) mod q
    w = pow(s, -1, q)

    # Calculate u1 = (hash * w) mod q
    u1 = (hash_value * w) % q

    # Calculate u2 = (r * w) mod q
    u2 = (r * w) % q

    # Calculate v = ((g^u1 * y^u2) mod p) mod q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

    # The signature is valid if v == r
    return v == r


public_key, private_key  = generate_dsa_key_pair()
k = random.randint(1, public_key[1])
message = "582346829557612"
message2 = "8161474912583"

r,s = sign_message(message, private_key[0], public_key,k)
r2,s2 = sign_message(message2, private_key[0], public_key,k)

h = int(hashlib.sha1(message.encode('utf-8')).hexdigest(), 16)
h2 = int(hashlib.sha1(message2.encode('utf-8')).hexdigest(), 16)

x2 = ((s*h2)-(s2*h)) * pow((r*s2-r2*s),-1,public_key[1])%public_key[1]
if(x2 == private_key[0]):
    print("The private key was found: ",x2)

m3 = "12345678910"

print("The attacker is now able to sign a message using the victim's private key")
signature = sign_message(m3, x2, public_key,random.randint(1, public_key[1]))
is_valid = verify_signature(m3, signature, public_key, private_key[1])
print("is valid: ",is_valid)
print("the attacker sent a message impersonating the victim: ",m3)

