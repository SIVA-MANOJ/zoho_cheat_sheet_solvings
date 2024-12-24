"""
Question Link:
https://www.geeksforgeeks.org/problems/twisted-prime-number/0

"""
def make_reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n//=10
    return rev


def isPrime(n):
    for i in range(2,round(n**0.5)+1):
        if n%i ==0:
            return False
    return True


num=101
if isPrime(num)==isPrime(make_reverse(num)):
    print("It is twisted prime number")
else:
    print("It is not a twisted prime number")