a,b=map(float,input().split())
p=lambda a,b:a*b/(a*b+(1-a)*(1-b))
print(p(a,b))
