# # Student Marks Analyzer

# # 1. Initialize an empty list to store marks
# marks_list = []

# # 2. Use a loop to ask for 5 subject marks
# print("Enter the marks for 5 subjects (out of 100):")

# for i in range(1, 6):
#     mark = float(input(f"Subject {i}: "))
#     marks_list.append(mark)

# # 3. Calculate Total and Average
# total_marks = sum(marks_list)
# average_marks = total_marks / 5

# # 4. Determine the Grade based on logic
# if average_marks >= 75:
#     grade = "Distinction"
# elif average_marks >= 60:
#     grade = "First Class"
# elif average_marks >= 40:
#     grade = "Pass"
# else:
#     grade = "Fail"

# # 5. Display the Results
# print("\n--- Results ---")
# print(f"Total Marks:   {total_marks}")
# print(f"Average Marks: {average_marks:.2f}")
# print(f"Final Grade:   {grade}")
# ________________________________________________
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