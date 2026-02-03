# name=input("enter your name:")
# age=input("enter your age:")
# print("hello " + name + " your age is " + age)

# problem 1: remove duplicates from list
nums=[1,1,2,3,4,4,5,5,6]
# nums=set(nums)
# nums=list(nums)
print(nums)
# without set()
if not nums:
    print([])
else:
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
nums=nums[:i+1]
print(nums) 

# problem 2:remove duplicates from tuple
