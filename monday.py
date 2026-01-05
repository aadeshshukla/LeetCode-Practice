# a=[12,43,21,55,78,90,33,67,89,100]
# even_numbers=[num for num in a if num%2==0]
# print(even_numbers)
# odd_numbers=[num for num in a if num%2!=0]
# print(odd_numbers)
# s=0
# total=[s:=s+num for num in a]
# print("Sum:",s)

#FREQUENCY COUNTER
# def frequency_counter(lst):
#     freq_dict = {}
#     for item in lst:
#         if item in freq_dict:
#             freq_dict[item] += 1
#         else:
#             freq_dict[item] = 1
#     return freq_dict
# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# result = frequency_counter(data)
# print(result) 

#FIND THE RUNNIG SUM
def running_sum(lst):
    running_total = 0
    result = []
    for num in lst:
        running_total += num
        result.append(running_total)
    return result
data = [1, 2, 3, 4]
print(running_sum(data))