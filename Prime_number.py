# Python3 program to print
# all primes less than N

# Function to check whether
# a number is prime or not .
#def isPrime(n):
#    if n<=1:
#        return False
#    for i in range(2,n):
#        if n%i == 0:
#            return False

#    return True
# Function to print primes
#def printPrime(n):
#    for i in range (2,n+1):
#       if isPrime(i):
#           print(i, end=" ")


      # Driver code
#if __name__ == "__main__":
#    n = 7
    # function calling
# printPrime(n)

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if(prime[p] == True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p +=1

    for p in range(2,n+1):
        if prime[p]:
            print(p)

# Driver code
if __name__ == '__main__':
    n = 20
    print("Following are the prime numbers smaller"),
    print("than or equal to", n)
    SieveOfEratosthenes(n)










