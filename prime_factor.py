"""
Prime factor – sort the array based on the minimum factor they have
"""
nums= [94,54,11,38,30,45,26]
fact_count_arr=[]
for num in nums:
    count=0
    for fact in range(1,num//2 +1):
        if num % fact ==0:
            count+=1
    fact_count_arr.append(count)
for i in range(len(fact_count_arr)):
    min=i
    for j in range(i+1,len(fact_count_arr)):
        if fact_count_arr[min] > fact_count_arr[j]:
            min=j
    fact_count_arr[i],fact_count_arr[min]= fact_count_arr[min],fact_count_arr[i]
    nums[i],nums[min]=nums[min],nums[i]
print(nums)
