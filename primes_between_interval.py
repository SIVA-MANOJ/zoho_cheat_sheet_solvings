"""
Question Link:-
https://www.geeksforgeeks.org/program-to-find-prime-numbers-between-given-interval/

Note:-(test cases: interval is negative in range)
"""
start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
print("YOUR PRIME NUMBERS")
k=0
for n in range(start,end+1):
   for i in range(2,n):
       if(n%i)==0:
           k=1
           break
       else:
           k=2
           continue
   if(k==2):
       print(n)