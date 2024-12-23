"""
Question Link:-
https://www.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0

"""

given_array=[5,5,6,2,8,1,9,4,7,1,9,1,8,7,4,4,7,3,4]
freq_dict={}
for i in given_array:
    if i not in freq_dict:
        freq_dict[i]=1
    else:
        freq_dict[i]+=1
# freq_dict = {5: 2, 6: 1, 2: 1, 8: 2, 1: 3, 9: 2, 4: 4, 7: 3, 3: 1}
d={}
for f in range(max(freq_dict.values()),0,-1):
    d[f]=[]
    for k in freq_dict:
        if f==freq_dict[k]:
            d[f]+=[k]
#d = {4: [4], 3: [1, 7], 2: [5, 8, 9], 1: [6, 2, 3]}
given_array=[]
for k in d:
    d[k].sort()
    for ele in d[k]:
        given_array+=[ele]*k

print(given_array)