# interview questions for python 
# 1. What is the difference between a list and a tuple in Python?
# A list is mutable, meaning it can be modified after creation, while a tuple is immutable, meaning it cannot be modified after creation.
#  Lists are defined using square brackets [], while tuples are defined using parentheses ().    

# 2. How do you handle exceptions in Python?
# In Python, exceptions can be handled using try-except blocks.
#  You can specify the type of exception you want to catch, and you can also use a generic except block to catch any exception.

# 3. What is a lambda function in Python?
# A lambda function is a small anonymous function that can have any number of arguments, but can only have one expression.
#  Lambda functions are defined using the lambda keyword, and they are often used for short, simple functions that are not reused elsewhere in the code.

# 4. What is the difference between a shallow copy and a deep copy in Python?
# A shallow copy creates a new object, but does not create copies of the objects that the original object references.
#  A deep copy creates a new object and also creates copies of the objects that the original object references.

# 5. How do you manage memory in Python?
# Python uses automatic memory management, which means that the Python interpreter takes care of allocating and deallocating memory as needed.
# However, you can manage memory in Python by:
# - Using generators instead of lists when dealing with large data sets, as generators do not store all values in memory at once.
# - Using the del statement to delete variables that are no longer needed, which can help free up memory.
# - Using the gc module to manually trigger garbage collection, which can help free up memory that is no longer being used.

# 6. What is the difference between a generator and a list comprehension in Python?
# A generator is an iterator that generates values on the fly, while a list comprehension creates a list in memory.

# 7. How do you optimize code for performance in Python?
# To optimize code for performance in Python, you can use techniques such as:
# - Using built-in functions and libraries, which are often optimized for performance.
# - Avoiding unnecessary computations and using efficient algorithms.
# - Using generators instead of lists when dealing with large data sets.
# - Using multiprocessing or multithreading to take advantage of multiple CPU cores.

# 8. What is the difference between a module and a package in Python?
# A module is a single file that contains Python code, while a package is a collection of modules organized in a directory hierarchy.
#  A module can be imported using the import statement, while a package can be imported using
# the import statement followed by the package name and the module name.

