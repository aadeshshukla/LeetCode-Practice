# palindrome number
def is_palindrome(num):
    # Convert the number to string
    str_num = str(num)
    
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]

# Test the function
test_numbers = [121, 12321, 123, 45654, 789]
for number in test_numbers:
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
        