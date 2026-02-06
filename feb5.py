# patter 1
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     print("*"*i)
# pattern 2
# ******
# *****
# ****
# ***
# **
# *
# rows=5
# for i in range(rows+1,0,-1) :
#     spaces=" "*(rows-1)
#     stars='*'*i
#     print(spaces+stars)
# pattern 3
# *****
#  ****
#   ***
#    **
#     *
# rows=5
# for i in range(1,rows+1) :
#     spaces=" "*(i-1)
#     stars='*'*rows
#     rows-=1
#     print(spaces+stars)
# pattern 4
#     *
#    ***
#   *****
#  *******
# rows=4
# for i in range(1,rows+1) :
#     spaces=" "*(rows-i)
#     stars='*'*(2*i-1)
#     print(spaces+stars)

# pattern 5
#     *
#    **
#   ***
#  ****
# *****
# rows=5
# for i in range(1,rows+1) :
#     spaces=" "*(rows-i)
#     stars='*'*i
#     print(spaces+stars)

# combine pattern 1 and 5 so we can print them side by side
# rows=5
# for i in range(1,rows+1) :
#     spaces=" "*(rows-i)
#     stars='*'*i
#     print(spaces+stars+"  "+stars)






