# Calculate Euler's totient function phi(m).

def gcd(a, b) :
    if b == 0: 
        return  a

    return gcd(b, a%b)

num = int(input("Enter the number : "))
cnt = 0

for i in range(1, num+1):
    if gcd(i, num) == 1 :
        cnt += 1

print("Euler's Totient is : ", cnt)
