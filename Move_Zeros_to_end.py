"""
Question Link:-
https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

"""
inp = [3, 5, 0, 0, 4]
p=len(inp)-1
for i in range(len(inp)):
    if i==p:
        break
    if inp[i]==0:
        inp[i],inp[p]=inp[p],inp[i]
        p-=1
print(inp)
