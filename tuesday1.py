# two sum problem 
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None
# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices of numbers that add up to {target}: {result}")

# three some problem
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result
# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(f"Triplets that sum to zero: {result}")

# merge two sorted lists
def merge_two_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list
# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = merge_two_sorted_lists(list1, list2)
print(f"Merged sorted list: {result}")

# we can also print time taken to execute each function
import time
start_time = time.time()
two_sum(nums, target)
end_time = time.time()
print(f"Time taken for two_sum: {end_time - start_time} seconds")
start_time = time.time()
three_sum(nums)
end_time = time.time()
print(f"Time taken for three_sum: {end_time - start_time} seconds")
start_time = time.time()
merge_two_sorted_lists(list1, list2)
end_time = time.time()
print(f"Time taken for merge_two_sorted_lists: {end_time - start_time} seconds")



