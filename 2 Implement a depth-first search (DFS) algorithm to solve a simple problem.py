def dfs(g,s,t,v=set()):
    v.add(s)
    if s==t:return[s]
    for n in g[s]:
        if n not in v:
            p=dfs(g,n,t,v)
            if p:return[s]+p

g={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['F'],'F':[]}
s,t='A','F'
p=dfs(g,s,t)
print(f"Path from {s} to {t}: {' -> '.join(p)}" if p else f"No path found from {s} to {t}.")
