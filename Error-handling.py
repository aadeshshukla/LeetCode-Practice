# Error handling in python 
try:    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError  
except ZeroDivisionError:  # Handling the specific exception
    print("Cannot divide by zero.")
except Exception as e:  # Handling any other exceptions
    print(f"An error occurred: {e}")   
else:  # Code that runs if no exceptions were raised
    print(f"The result is: {result}")   
finally:  # Code that runs regardless of whether an exception was raised or not
    print("This will always be executed.")

# lets do an example of password validation using error handling
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    return "Password is valid."
# Example usage
try:
    password = "Passw0rd"
    print(validate_password(password))
except ValueError as e:
    print(f"Error: {e}")
