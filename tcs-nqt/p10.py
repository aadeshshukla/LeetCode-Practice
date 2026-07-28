# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         i = 0  # Points to where the next non-zero element should go
        
#         for j in range(len(nums)):
#             if nums[j] != 0:
#                 # Swap the non-zero element into position i
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1  # Move slow pointer forward

# # Example usage
# solution = Solution()
# nums = [0, 1, 0, 3, 12]
# solution.moveZeroes(nums)
# print(nums)  # Output: [1, 3, 12, 0, 0]
l1=[1,3,5,7,9]
l2=[8,6,4,2,0]

def mergetwo(a,b):
    i=0
    j=len(b)-1
    result=[]
    while i<len(a) and j>=0:
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j-=1
        while i<len(a):
            result.append(a[i])
            i+=1
        while j>=0:
            result.append(b[j])
    return result
print(mergetwo(l1,l2))