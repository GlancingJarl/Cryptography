
import math
#create a  main function
root = 25




def main():
    #create a list
    list = []
    #create a for loop
    for i in range(1,root):
        #create a if statement
        if isPrimitiveRoot(i,root):
            #append the list
            list.append(i)
    #print the list
    
    print("the primitive roots of " + str(root) + " is: " + str(list))
    

def isPrimitiveRoot(a, p):
    """
    Check if a is a primitive root of p
    """
    greatest = math.gcd(a, p)
    if greatest != 1:
        print("GCD of "+str(a)+" and "+str(p)+" is "+str(greatest))
        return False
    # Euler's totient function
    phi = p
    phifactors = factorsfunc(phi)
    for factor in phifactors:
        if factor != 1:
            phi = phi * (1 - 1 / factor)
    phi = int(phi)
    factors = factorsfunc(phi)
    for factor in factors:

        if pow(a, factor, p) == 1:
            print(str(a)+"^"+str(factor)+" mod "+str(p)+" = 1 therefore "+str(a)+" is not a primitive root of "+str(p)+"\n")
            return False
    #combine every power of a mod p in a single string and then print it
    powers = []
    for i in range(1, phi + 1):
        powers.append(str(pow(a, i, p)))
    print("Powers of "+str(a)+" mod "+str(p)+": "+", ".join(powers) )
    print("since "+str(a)+"^20 mod 25 = 1 then "+ str(a) + " is a primitive root" +"\n")

    return True
    


def factorsfunc(n):
    """
    Return a list of factors of n
    """
    return [i for i in range(1, n) if n % i == 0]
main()    