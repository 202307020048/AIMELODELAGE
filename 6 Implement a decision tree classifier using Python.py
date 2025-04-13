from sklearn.tree import DecisionTreeClassifier as D
from sklearn.datasets import load_iris as l
from sklearn.model_selection import train_test_split as s

X,y=l(return_X_y=True)
a,b,c,d=s(X,y,test_size=0.2,random_state=42)
m=D().fit(a,c)
print(m.predict(b))
