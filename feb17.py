# interview level: easy
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# code
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]
# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False

# time complexity: O(n)
# space complexity: O(n)


# dictionary problems
def count_occurrences(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
# Test case
print(count_occurrences("hello world"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# 2. Given a list of integers, return a new list containing only the unique elements from the original list.
def unique_elements(lst):
    unique_set = set()
    unique_list = []
    for num in lst:
        if num not in unique_set:
            unique_set.add(num)
            unique_list.append(num)
    return unique_list
# Test case
print(unique_elements([1, 2, 3, 2, 4, 1, 5]))  # Output: [1, 2, 3, 4, 5]

# 3. Given a list of words, return a dictionary where the keys are the words and the values are the lengths of those words.
def word_lengths(words):
    length_dict = {}
    for word in words:
        length_dict[word] = len(word)
    return length_dict
# Test case
print(word_lengths(["hello", "world", "python"]))  # Output: {'hello': 5, 'world': 5, 'python': 6}

# 4. Given a list of integers, return a dictionary where the keys are the integers and the values are the number of times each integer appears in the list.
def count_integers(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
# Test case
print(count_integers([1, 2, 3, 2, 4, 1, 5]))  # Output: {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}
