x=[4,5,6,3,6,3]
y=[10,19,18,15,18,15]
n=len(x)
sx=sum(x)
sy=sum(y)
ax=sx/n
ay=sy/n

sxy=0
sxx=0
for i in range(n):
    xy=x[i]*y[i]
    sxy=sxy+xy
for i in range(n):
    xx=x[i]*x[i]
    sxx=sxx+xx
ssx=sx*sx
nu=(n*sxy)-(sx*sy)
print(nu)
de=n*sxx-(ssx)
print(de)
m=nu/de
print(m)
b=ay-(m*ax)
print(b)
x_new=int(input("enter new value of x"))
y_pred=(m*x_new)+b
print(f"predicted value of y is {y_pred}")
# 
# 
# 
# 
# 
# 