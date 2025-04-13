import random as r
u=input();c=r.choice(['r','p','s'])
print(c,["tie","win","lose"][("rps".index(u[0])- "rps".index(c[0]))%3])
