"""
Question Link:
https://www.geeksforgeeks.org/find-number-currency-notes-sum-upto-given-amount/

"""

currency_notes=[2000, 500, 200, 100, 50, 20, 10, 5, 1]
inp=2456
ans={2000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}

while inp>0:
    for i in currency_notes:
        if inp>=i:
            ans[i]+=1
            inp=inp-i
            break
print(ans)