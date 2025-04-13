from collections import deque
import random as r

Q={},a=deque,max
def ql(s,a_,r_,s_,A,g=0.9,a=0.1):
 Q.setdefault(s,{b:0 for b in A})
 Q.setdefault(s_,{b:0 for b in A})
 Q[s][a_]+=(a*(r_+g*m(Q[s_].values())-Q[s][a_])
