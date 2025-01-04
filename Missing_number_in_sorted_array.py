"""
Question Link:-
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

"""
n=5
arr=[1,2,3,4]
temp=True
if len(arr)==n:
    print("Nothing is missing")
else:
    for i in range(n-1):
        if arr[i]!=i+1:
            print(i+1)
            temp=False
            break
    if temp:
        print(n)
#or
print(set(range(1,n+1)).difference(set(arr)).pop())