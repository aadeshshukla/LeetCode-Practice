# Python code for LeetCode problems
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the numbers
        num_dict = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # If not, add the current number and its index to the dictionary
            num_dict[num] = i
        
        # Return an empty list if no solution is found
        return []
    def reverse(self, x: int) -> int:
        # Convert the integer to a string and reverse it
        sign = -1 if x < 0 else 1
        x_str = str(abs(x))[::-1]
        
        # Convert the reversed string back to an integer
        reversed_x = sign * int(x_str)
        
        # Check for overflow and return 0 if it occurs
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        x_str = str(x)
        
        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numerals to their corresponding values
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the string from right to left
        for char in reversed(s):
            value = roman_dict[char]
            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Start with the first string as the longest common prefix
        prefix = strs[0]
        # Iterate through the list of strings
        for s in strs[1:]:
            # Update the prefix by comparing it with the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping:
                    return False
            else:
                stack.append(char)
        return not stack
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1