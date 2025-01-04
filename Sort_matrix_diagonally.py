"""
Question Link:-
https://leetcode.com/problems/sort-the-matrix-diagonally/description/

"""
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
i=0
j=0
temp=[]
res=[[0]*len(mat[0]) for _ in range(len(mat))]
for c in range(len(mat[0])):
    i=0
    j=c
    while i<len(mat) and j<len(mat[0]):
        temp.append(mat[i][j])
        i+=1
        j+=1
        
    i-=1
    j-=1
    while i>=0:
        res[i][j]=max(temp)
        temp.remove(max(temp))
        i-=1
        j-=1

for r in range(len(mat[0])):
    i=r
    j=0
    while i<len(mat) and j<len(mat[0]):
        temp.append(mat[i][j])
        i+=1
        j+=1
    
    i-=1
    j-=1
    while j>=0:
        res[i][j]=max(temp)
        temp.remove(max(temp))
        i-=1
        j-=1
print(res)