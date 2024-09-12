x=(1,(2,3),(4,5,6))
y=list(x)
print(y)
final=[]
for p in y:
    if isinstance(p,list):
        final.extend(p)
    elif isinstance(p,tuple):
        final.extend(p)
    else:
        final.append(p)
print(final)
z=tuple(final)
print(z)
print(type(z))               