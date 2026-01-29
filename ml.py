# import matplotlib.pyplot as plt 

# x = [1, 2, 3, 4]
# y = [10, 15, 7, 20]
# plt.plot(x, y, marker='o', label='sales', linestyle='-', color='b')
# plt.xlabel('Month')
# plt.ylabel('Revenue')
# plt.title('Monthly Sales')
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.6) 
# plt.show()

# import math
# sqrt_value=math.sqrt(25)
# print(f"square root of 25:{sqrt_value:.2f}")
# factorial_value=math.factorial(5)
# print(f"factorial of 5:{factorial_value}")
# angle_radians=math.radians(30)
# sine_radians=math.sin(angle_radians)
# print(f"sin of 30 degrees :{sine_radians}")

# import numpy as np 

# # Creating a 1D array
# arr1d = np.array([1, 2, 3])
# print(f"1D array:\n{arr1d}")

# # Creating a 2D array
# arr2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(f"\n2D array:\n{arr2d}")

# import scipy.optimize as opt
# from scipy.integrate import quad
# def objective(x):
#     return x[0]**2 + x[1]**2
# res_min = opt.minimize(objective, [1, 1])
# print(f"Optimal solution: {res_min.x}")
# def integrand(x):
#     return x**2
# area, error = quad(integrand, 0, 2)
# print(f"Integral result: {area:.2f}")
# print(f"Estimated error: {error:.2e}")

# import pandas as pd
# data={'name':['alice','bob','jhon'],
#        'age':[23,25,22]}
# df=pd.DataFrame(data)
# print(df)

import statistics

def calculate_mean(data): 
    return sum(data) / len(data)

def calculate_median(data): 
    sorted_data = sorted(data) 
    n = len(sorted_data)

    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1] 
        middle2 = sorted_data[n // 2] 
        return (middle1 + middle2) / 2
    else:
        return sorted_data[n // 2]

def calculate_mode(data):
    return statistics.mode(data)

def calculate_variance(data):
    mean_value = calculate_mean(data)
    # Fixed the encoding character in 'diff'
    squared_diff_sum = sum((x - mean_value) ** 2 for x in data) 
    return squared_diff_sum / (len(data) - 1)

def calculate_standard_deviation(data): 
    variance_value = calculate_variance(data) 
    return variance_value ** 0.5

# Example dataset
dataset = [10, 20, 30, 40, 50]

mean_value = calculate_mean(dataset) 
median_value = calculate_median(dataset) 
mode_value = calculate_mode(dataset) 
variance_value = calculate_variance(dataset)
std_deviation_value = calculate_standard_deviation(dataset)

print(f"Dataset: {dataset}") 
print(f"Mean: {mean_value:.2f}") 
print(f"Median: {median_value:.2f}") 
print(f"Mode: {mode_value}") 
print(f"Variance: {variance_value:.2f}")
print(f"Standard Deviation: {std_deviation_value:.2f}")