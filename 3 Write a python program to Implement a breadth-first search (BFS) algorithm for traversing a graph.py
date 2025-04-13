def b(g,s):
 r=[s];v={s}
 while r:
  n=r.pop(0);print(n,end=' ')
  for x in g[n]:
   if x not in v:v.add(x);r+=[x]

g={0:[1,2],1:[0,2],2:[0,1]}
print("\nTest Case 4:")
b(g,0)
