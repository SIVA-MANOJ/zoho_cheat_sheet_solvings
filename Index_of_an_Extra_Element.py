"""
Question Link:-
https://www.geeksforgeeks.org/problems/index-of-an-extra-element/1

Note:- You have given two sorted arrays arr1[] & arr2[] of distinct elements.
The first array has one element extra added in between. Return the index of the extra element.
"""
inp1 = [2,4,6,8,9,10,12]
inp2 = [2,4,6,8,10,12]
print(inp1.index((set(inp1).difference(set(inp2)).pop())))
