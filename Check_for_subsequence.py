"""
Question Link:
https://www.geeksforgeeks.org/problems/check-for-subsequence/0

"""
str1='gksrek'
str2='geeksforgeeks'
i=0
for ch in str2:
    if ch==str1[i]:
        i+=1
        if i==len(str1):
            break

if i==len(str1):
    print("subsequence") #print(1)
else:
    print("not subsequence")  #print(0)