# 120 chars

D=1000
V,L=[0],[0]+[-1]*D
for i in range(D):
	D=V[i]
	if L[D]==-1:V.append(0)
	else:V.append(i-L[D])
	print(V[i]);L[D]=i