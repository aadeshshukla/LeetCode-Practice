# dsa problems pattern 1
# 1. find the largest sum of contiguous subarray of size k
def largest_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - (k - 1)]
    return max_sum
a=[2, 1, 5, 1, 3, 2]
k=3
print(largest_sum_subarray(a, k))

# 2. find the smallest sum of contiguous subarray of size k
def smallest_sum_subarray(arr, k):
    min_sum = float('inf')
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k - 1:
            min_sum = min(min_sum, window_sum)
            window_sum -= arr[i - (k - 1)]
    return min_sum
a=[2, 1, 5, 1, 3, 2]
k=3
print(smallest_sum_subarray(a, k))

# 3. find the longest substring with k distinct characters
def longest_substring_k_distinct(s, k):
    char_count = {}
    left = 0
    max_length = 0
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
s = "eceba"
print(longest_substring_k_distinct(s, 2))

# sliding window pattern 2
# 1. find the smallest window in a string containing all characters of another string
def min_window(s, t):
    from collections import Counter
    t_count = Counter(t)
    window_count = {}
    have, need = 0, len(t_count)
    left = 0
    min_length = float('inf')
    min_window_start = 0

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            have += 1

        while have == need:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                min_window_start = left

            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    return s[min_window_start:min_window_start + min_length] if min_length != float('inf') else ""
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))
