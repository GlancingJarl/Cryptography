import hashlib
import math


def baby_step_giant_step(p, g, A):
    # Step 1: Compute m = ceil(sqrt(q))
    m = math.ceil(math.sqrt(p-1))

    # Step 2: Compute the baby steps
    baby_steps = {}
    for i in range(m):
        baby_steps[pow(g, i, p)] = i

    # Step 3: Compute the giant steps
    gm = pow(g, m * (p-2), p)
    
    for i in range(m):
        giant_step = ((A * pow(gm,i,p)) % p)
        if giant_step in baby_steps:
            print("found match", giant_step, "at index", i)
            return i*m + baby_steps[giant_step]

    return None

def signDoc(D, k, x, p, q, g):
    r = pow(g, k, p) % q
    
    dHash = int(hashlib.sha1(str(D).encode('utf-8')).hexdigest(), 16)


    s = (pow(k, -1, q) * (dHash + x * r)) % q
    return r, s



# Example usage
p = 103687
q = 1571
g = 21947
A = 31377
D = 510
k = 1105

x = baby_step_giant_step(p, g, A)
print("The solution to the discrete log problem is:", x)
a,b = signDoc(D, k, x, p, q, g)

print("The signature is:")
print("r = ", a)
print("s = ", b)
