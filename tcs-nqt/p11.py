def find_max_avg(nums , k):
    i=0
    curr_sum=0
    n=len(nums)
    for i in range(k):
        curr_sum+=nums[i]
    max_avg=curr_sum/k
    for i in range(k,n):
        curr_sum+=nums[i]
        curr_sum-=nums[k-i]
        curr_avg=curr_sum/k
    max_avg=max(max_avg,curr_avg)
    return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
print(find_max_avg(nums,k))

