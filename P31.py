# Determine whether a given integer number is prime.

from math import sqrt

def isPrime(num) :
    '''A function to check whether a number is Prime or not.'''

    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            # If num is divisible by any number other than itself, return False.
            if num % i == 0:
                return False
        return True
    else:
        return False

num = int(input("Enter the number : "))

if isPrime(num):
    print("The number is Prime")
else :
    print("The number is Not Prime")
