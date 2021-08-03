# Determine the prime factors of a given positive integer (2).
from math import sqrt
from collections import Counter

def primeFactors(n):
    '''A function to calculate Prime Factors of a number
    along with their frequency.'''

    arr = []
    while n % 2 == 0:
        arr.append(2)
        n /= 2
         
    # n will be odd now so a skip of 2 can be done
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            arr.append(i)
            n /= i

    if n > 2:
        arr.append(n)
    
    return arr


num = int(input("Enter the number : "))
ans = []

print(f"Prime Factors of {num} are:", end=" ")

# Create a frequency dictionary where key is the prime factor
# and value is the count of that factor.
counter_dict = Counter(primeFactors(num))

# Store the factor and it's frequency as a tuple in an array.
for k, v in counter_dict.items():
    ans.append((k, v))

print(ans)

