"""
Question URL:
https://www.geeksforgeeks.org/problems/special-array-reversal/0

"""

src="A&x#"
des=''
f,r=0,len(src)-1
while f<len(src):
    if src[f].isalpha():
        if src[r].isalpha():
            des+=src[r]
            r-=1
            f+=1
        else:
            r-=1
    else:
        des+=src[f]
        f+=1
print(des) # x&A#