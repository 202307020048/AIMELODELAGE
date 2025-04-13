def d(m,s,e,v=set()):
 if s==e:return[s]
 v.add(s)
 for n in m.get(s,[]):
  if n not in v:
   p=d(m,n,e,v)
   if p:return[s]+p

def b(m,s,e):
 q=[[s]];v={s}
 while q:
  p=q.pop(0);n=p[-1]
  if n==e:return p
  for x in m.get(n,[]):
   if x not in v:v.add(x);q+=[p+[x]]

# example maze as graph
m={0:[1],1:[0,2],2:[1,3],3:[]}
print("DFS:",d(m,0,3))
print("BFS:",b(m,0,3))
