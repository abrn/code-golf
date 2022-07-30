# 331 chars

b,w='bottles of beer','on the wall'
m,t,l,k='more','Take one down and pass it around, ','1 bottle of beer',f'{b} {w}'
for i in range(99,2,-1):
    print(f'{i} {k}, {i} {b}.\n{t}{i-1} {k}.\n')
print(f'2 {k}, 2 {b}.\n{t}{l} {w}.\n\n{l} {w}, {l}.\n{t}no {m} {k}.\n\nNo {m} {k}, no {m} {b}.\nGo to the store and buy some {m}, 99 {k}.')