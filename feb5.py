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
rows=5
for i in range(rows+1,0,-1) :
    spaces=" "*i
    stars='*'*rows
    rows=rows-1
    print(spaces+stars)

