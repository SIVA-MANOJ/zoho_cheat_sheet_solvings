"""
Qusetion Link:-
https://leetcode.com/problems/single-element-in-a-sorted-array/description/

"""
inp=[3,3,7,7,10,11,11]
for i in range(0,len(inp),2):
    if inp[i]!=inp[i+1]:
        break
print(inp[i])
