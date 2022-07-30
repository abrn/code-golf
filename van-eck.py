# 136 chars

D=1000
v,l=[0],[0]+[-1]*D
for i in range(D):
    c=v[i]
    if l[c]==-1:v.append(0)
    else:v.append(i-l[c])
    print(v[i])
    l[c]=i