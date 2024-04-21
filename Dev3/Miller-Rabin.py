import random


def main():
    
    #genrate a random 15 bit number until one is prime
    #print the prime number
   
    v = False
    while not v:
        b = random.getrandbits(15)
        test = millerRabin(b)
        if test:
            v = True
            print("generated prime:",b)


    

def millerRabin(n, k=6):
    # Check if n is even or less than or equal to 1
    if n <= 1 or n % 2 == 0:
        return False

    
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False

    return True
    
main()
