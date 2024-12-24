"""
Question Link:
https://www.geeksforgeeks.org/program-to-print-first-n-prime-numbers/
"""

nop=10
natural_number=2
while nop>0:
    prime=True
    for j in range(2,natural_number):
        if natural_number%j==0:
          prime=False
          break
    if prime:
        nop-=1
        print(i)
    natural_number+=1