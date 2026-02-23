# python random problems:
# 1. Write a Python program to generate a random number between 1 and 100.
import random
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
# 2. Write a Python program to shuffle a list of numbers from 1 to 10.
numbers = list(range(1, 11))
random.shuffle(numbers)
print(f"Shuffled list of numbers from 1 to 10: {numbers}")
# 3. Write a Python program to simulate rolling a six-sided die.
die_roll = random.randint(1, 6)
print(f"Rolling a six-sided die: {die_roll}")
# 4. Write a Python program to generate a random password of length 8.
import string
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
random_password = generate_random_password()
print(f"Random password of length 8: {random_password}")
# 5. Write a Python program to simulate a coin flip.
coin_flip = random.choice(['Heads', 'Tails'])
print(f"Simulating a coin flip: {coin_flip}")
