from collections import deque
g=[[0,0,0],[0,1,0],[0,0,0]];v={(0,0)};q=deque([(0,0)]);d=[(0,1),(1,0),(-1,0),(0,-1)]
while q:
 x,y=q.popleft()
 if g[x][y]==1:print('Wumpus!');break
 for i,j in d:
  a,b=x+i,y+j
  if 0<=a<3 and 0<=b<3 and (a,b)not in v:
   v.add((a,b));q.append((a,b))
