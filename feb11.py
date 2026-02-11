# dsa  problems level 2
# problem: Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
# Example usage:
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3 (the longest substring is "abc")
# problem: Given a string s, find the length of the longest substring that contains at most two distinct characters.
def lengthOfLongestSubstringTwoDistinct(s):
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
# Example usage:
s = "eceba"
print(lengthOfLongestSubstringTwoDistinct(s))  # Output: 3 (the longest substring is "ece")
# dsa  problems level 3
# problem: Given a string s, find the length of the longest substring that contains at most k distinct characters.
def lengthOfLongestSubstringKDistinct(s, k):
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
# Example usage:
s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))  # Output: 3 (the longest substring is "ece")
