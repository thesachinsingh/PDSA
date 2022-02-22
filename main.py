# A positive integer m is a prime product if it can be written as pxq,
# where p and q are both primes..

# Write a Python function prime_product(m) that takes an integer m as input
#  and returns True if m is a prime product and False otherwise. 
# (If m is not positive, function should return false.)
# def prime_product(m):

def isPrime(n):
    flag = True
    i=2
    while(i < ((n//2) + 1)):
        if n % i == 0:
            flag = False
            break
        i+=1
    return flag

def factors(k):
    f = []
    for i in range(2, ((k//2) + 1)):
        if k%i==0:
            f.append(int(i))
    print(f'Factors of {k} : {f}')


def prime_product():
    m = int(input("Enter number to factorize : "))
    for i in range(2, ((m//2) + 1)):
        if m % i == 0 and isPrime(int(i)) and isPrime(int(m/i)):
            print("Mentioned No. is a prime product")
            factors(m)
            return True
            break
    print(False)

prime_product()