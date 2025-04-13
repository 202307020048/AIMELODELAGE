from sklearn.svm import SVC
X=[[0,0],[1,1]]
y=[0,1]
m=SVC().fit(X,y)
print(m.predict([[0.5,0.5]]))
