"""
Question link:

"""
ques=[131, 11, 48]
ans=set()
for num in ques:
    while num>0:
        digit=num%10
        ans.update({digit})
        num=num//10
print(ans)