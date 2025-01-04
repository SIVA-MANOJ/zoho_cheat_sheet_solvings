"""
Question Link:-
https://leetcode.com/problems/single-number-ii/description/

"""
inp=[0,1,0,1,0,1,99]
d={}
for i in inp:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]==1:
        print(i)
        break
