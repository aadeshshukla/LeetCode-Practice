# lets write an program which guesses the number which user has in mind , user will tell only its higher or lower than the guess of program 
import random
def guess_number():
    lower_limit = 1
    upper_limit = 100
    attempts = 0
    print("Think of a number between 1 and 100, and I will try to guess it.")
    # give the user some time to think of a number
    input("Press Enter when you're ready.")
    while True:
        guess = random.randint(lower_limit, upper_limit)
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is your number higher, lower, or correct? (h/l/c): ").lower()
        if feedback == 'h':
            lower_limit = guess + 1
        elif feedback == 'l':
            upper_limit = guess - 1
        elif feedback == 'c':
            print(f"Congratulations! I guessed your number in {attempts} attempts.")
            break
        else:            print("Invalid input. Please enter 'h' for higher, 'l' for lower, or 'c' for correct.")
guess_number()

# is there any way to optimize this code ?
# Yes, we can optimize the code by using a binary search algorithm instead of random guessing.
def optimized_guess_number():
    lower_limit = 1
    upper_limit = 100
    attempts = 0
    print("Think of a number between 1 and 100, and I will try to guess it.")
    input("Press Enter when you're ready.")
    while lower_limit <= upper_limit:
        guess = (lower_limit + upper_limit) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is your number higher, lower, or correct? (h/l/c): ").lower()
        if feedback == 'h':
            lower_limit = guess + 1
        elif feedback == 'l':
            upper_limit = guess - 1
        elif feedback == 'c':
            print(f"Congratulations! I guessed your number in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please enter 'h' for higher, 'l' for lower, or 'c' for correct.")
optimized_guess_number()

