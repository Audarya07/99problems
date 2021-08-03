# Determine the greatest common divisor of two positive integer numbers.

def gcd(a, b) :
    '''A function to calculate GCD of 2 numbers.
    
    Parameters:
        a (int): First number
        b (int): Second number
    
    Returns:
        gcd(a, b): GCD of 2 numbers a and b
    '''
    
    if b == 0 :
        return  a
    else: 
        return gcd(b, a%b)

a = int(input("Enter first number : "))
b = int(input("Enter Second number : "))

print(f'The GCD of {a} and {b} is : {gcd(a, b)}')
