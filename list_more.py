# a=[1,2,3,2,4,5,6,4,5,6,7,8,9,7,8,9]
# b=set(a)
# a=list(b)
# print(a)       
#_____________________________________________________
# Remove Duplicates: How to modify a list in-place without using extra memory
# a=[1,2,3,2,4,5,6,4,5,6,7,8,9,7,8,9]
# i=0
# while i < len(a):
#     j = i + 1
#     while j < len(a):
#         if a[i] == a[j]:
#             a.pop(j)
#         else:
#             j += 1
#     i += 1
# print(a)
#______________________________________________________________
a=[1,2,3,2,4,5,6,4,5,6,7,8,9,7,8,9]
a.sort()
i=0
while i < len(a)-1:
    if a[i] == a[i+1]:
        a.pop(i+1)
    else:
        i += 1
print(a)
#_______________________________________________________________
# Move Zeroes: Given an array, move all 0's to the end while maintaining the relative order of non-zero elements.
a=[0,1,0,3,12]
i=0
for j in range(len(a)):
    if a[j] != 0:
        a[i] = a[j]
        i += 1
for k in range(i, len(a)):
    a[k] = 0
print(a)