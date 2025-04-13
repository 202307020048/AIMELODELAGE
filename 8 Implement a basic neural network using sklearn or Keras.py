from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[1],[1],[0]])
m=Sequential([Dense(8,input_shape=(2,),activation='relu'),Dense(1,activation='sigmoid')])
m.compile('adam','mse')
m.fit(x,y,epochs=100,verbose=0)
print(m.predict(x).round())
