# 106 chars

print(0)
x=lambda n,x=(0,1):[x:=(x[1],sum(x)) for i in range(n+1)][-1][0]
for i in range(0,30):print(x(i))