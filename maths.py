# lets write code for maths formulas 
# code to find the area of a circle
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

# code to find the circumference of a circle
def circumference_of_circle(radius):
    return 2 * math.pi * radius

# code to find the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# code to find the perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# code to find the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# code to find the perimeter of a triangle
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

# code to find the area of a square
def area_of_square(side):
    return side ** 2

# code to find the perimeter of a square
def perimeter_of_square(side):
    return 4 * side

# code to find the area of a parallelogram
def area_of_parallelogram(base, height):
    return base * height

# code to find the perimeter of a parallelogram
def perimeter_of_parallelogram(side1, side2):
    return 2 * (side1 + side2)

# area of triangle using heron's formula
def area_of_triangle_heron(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# lcm
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# hcf
def hcf(a, b):
    return math.gcd(a, b)

# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# power
def power(base, exponent):
    return base ** exponent

# code to solve quadratic equation
def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No real roots"
    elif d == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2

# code to find the distance between two points
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# code to find the midpoint between two points
def midpoint_between_points(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

# code to find the slope of a line
def slope_of_line(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined"
    else:
        return (y2 - y1) / (x2 - x1)
    
# code to find factors of a number
def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

# code to find prime factors of a number
def prime_factors(n):
    result = []
    for i in range(2, n + 1):
        while n % i == 0:
            result.append(i)
            n //= i
    return result

# code to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# code to find the sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# code to find the product of digits of a number
def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

# code to find the reverse of a number
def reverse_number(n):
    return int(str(n)[::-1])

# code to check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# code to find the gcd of two numbers
def gcd(a, b):
    return math.gcd(a, b)

# code to find determinant of a 2x2 matrix
def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matrix must be 2x2")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# code to find determinant of a 3x3 matrix
def determinant_3x3(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        raise ValueError("Matrix must be 3x3")
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

# code to find the inverse of a 2x2 matrix
def inverse_2x2(matrix):
    det = determinant_2x2(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    return [[matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]]

# code to find the inverse of a 3x3 matrix
def inverse_3x3(matrix):
    det = determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    inv = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    inv[0][0] = (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) / det
    inv[0][1] = (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) / det
    inv[0][2] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) / det
    inv[1][0] = (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) / det
    inv[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) / det
    inv[1][2] = (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) / det
    inv[2][0] = (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) / det
    inv[2][1] = (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) / det
    inv[2][2] = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) / det
    return inv

# code to find the transpose of a matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# code to find logarithm of a number
def logarithm(value, base=math.e):
    if value <= 0:
        raise ValueError("Logarithm is undefined for non-positive values")
    return math.log(value, base)

print(logarithm(100, 10))  # Output: 2.0
m=[[1, 2, 3], [0, 1, 4], [5, 6, 0]]
print(inverse_3x3(m))


# code to find bitwise AND of two numbers
def bitwise_and(a, b):
    return a & b

# code to find bitwise OR of two numbers
def bitwise_or(a, b):
    return a | b

    