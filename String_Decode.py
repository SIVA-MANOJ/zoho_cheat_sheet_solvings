"""
Question Link:
https://www.geeksforgeeks.org/problems/decode-the-string2444/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

"""
string = "3[b2[ca2[k]]]"
res=''
for i in string[::-1]:
  if i=='[' or i==']':
    continue
  elif i in "abcdefghijklmnopqrstuvwxyz":
    res=res+i
  elif i in "123456789":
    res=int(i)*res
print(res[::-1])