# lst=[1,2,3,4,5]
# target=5
# def search(lst, target):
#     left, right = 0, len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# result = search(lst, target)
# print(f"Target {target} found at index: {result}")
#_____________________________________________________________
# lst=[1,2,3,4,5]
# target=5
# r=[]
# for i in range(len(lst)-1):
#     if lst[i]+lst[i+1]==target:
#         r.append(lst[i])
#         r.append(lst[i+1])
# print(r) 
#___________________________________________________-
# lst=[1,2,3,4,5]
# target=5
# a=[]

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             b=[]
#             b.append(lst[i])
#             b.append(lst[j])
#             a.append(b)
        
# print(a)