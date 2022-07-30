# 323 chars

H=print
B,D='bottles of beer','on the wall'
C,E,F,A='more','Take one down and pass it around, ','1 bottle of beer',f"{B} {D}"
for G in range(99,2,-1):H(f"{G} {A}, {G} {B}.\n{E}{G-1} {A}.\n")
H(f"""2 {A}, 2 {B}.
{E}{F} {D}.

{F} {D}, {F}.
{E}no {C} {A}.

No {C} {A}, no {C} {B}.
Go to the store and buy some {C}, 99 {A}.""")