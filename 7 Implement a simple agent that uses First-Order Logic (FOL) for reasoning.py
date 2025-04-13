from sympy import symbols, Implies, And, Or, Not, satisfiable
a,b,c = symbols('a b c')
kb = And(Implies(a,b), Implies(b,c), a)
q = c
print(satisfiable(And(kb, Not(q))) == False)
