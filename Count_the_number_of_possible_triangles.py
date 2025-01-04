"""
Question Link:-
https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

"""
import math
given=[65,1,11,1,5,6]
filarr=list(set(given))
if len(filarr)<3:
  print(0)
else:
  if len(filarr)==3:
    print(1)
  else:
    denom=6*(math.factorial(len(filarr)-3))
    res=math.factorial(len(filarr)) / denom
    print(int(res)) #permutaion & combination concept