"""
Question link:
https://www.geeksforgeeks.org/problems/sort-in-specific-order/0

"""
ques=[1, 2, 3, 5, 4, 7, 10]
odd_arr=[i for i in ques if i%2!=0]
even_arr=[i for i in ques if i%2==0]

odd_arr.sort()  # instead of this use your own sorting function
even_arr.sort() # instead of this use your own sorting function

res=odd_arr[::-1]+even_arr
print(res)