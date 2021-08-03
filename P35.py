# Determine the prime factors of a given positive integer.
from math import sqrt

def primeFactors(n):
    '''A function to calculate Prime Factors of a number.'''

    # If n is divisible by 2, print 2, divide n by 2
    # and repeat.
    while n % 2 == 0:
        print(2, end=" ")
        n /= 2
         
    # n will be odd now so a skip of 2 can be done
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            print(i, end=" ")
            n /= i

    if n > 2:
        print(n)


num = int(input("Enter the number : "))

print(f"Prime Factors of {num} are:", end=" ")
primeFactors(num)
print()
