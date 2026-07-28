def minimumSwap (nums):
    i=0
    j=len(nums)-1
    count=0
    while i<j:
        while i<j and nums[i]!=0:
            i+=1
        while i<j and nums[j]==0:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
            count+=1
            i+=1
            j-=1
    return count

nums = [0, 1, 0, 1, 1, 0]
print(minimumSwap(nums))
