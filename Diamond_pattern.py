"""
Question link:
https://www.geeksforgeeks.org/program-print-diamond-shape/
"""

n=11        # number of stars in a row
for i in range(n):      # i --> row
    for j in range(n):      # j --> column
        if (i+j>=n//2 and j-i<=n//2)and(i-j<=n//2 and i+j<=n+((n//2)-1)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
