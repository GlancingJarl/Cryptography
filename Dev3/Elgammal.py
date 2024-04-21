import random

from Crypto.Util.number import inverse


q = 89
a = 13
k = 43

def main():
    m1 = 80
    print("Original message:", m1)

    # Generate keys
    private_key = random.randint(1, q-1)
    public_key = pow(a, private_key, q)

    # Encrypt message
    r = pow(a, k, q)
    c = (m1 * pow(public_key, k,q)) % q

    # Decrypt message
    s = pow(r, private_key, q)
    #get the modular inverse of s
    s_inv = inverse(s,q)
    decrypted_message = (s_inv * c) % q
    print("Decrypted message:", decrypted_message)


main()