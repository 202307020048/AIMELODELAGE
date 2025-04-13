from collections import deque
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
q = deque()
q.append(clf.fit(X_train, y_train))
