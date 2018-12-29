import os
import numpy as np
from tensorflow.python.framework import ops
import matplotlib.pyplot as plt
import tqdm
import keras



from keras.models import Sequential
from keras.layers import Dense

''''
X=[
    [[0],[0]],
    [[1],[0]],
    [[0],[1]],
    [[1],[1]]
]
Y=[
    [0],
    [1],
    [1],
    [0]
]
'''
X=[[0,0],[1,0],[0,1],[1,1]]
Y=[[1,0,0],[0,1,0],[0,1,0],[1,0,0]]
print(X[0])
print(Y[0])



# create model
model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(3, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=600, batch_size=2,verbose=2)


newn=np.array([[0,1],[1,0]])
#np.shape(newn)
print(newn)
#predictions= model.
predictions = model.predict(newn)
# round predictions
print(predictions)
rounded = [round(x[1]) for x in predictions]
print(rounded)


# Генерируем описание модели в формате json
#model_json = model.to_json()
# Записываем модель в файл
#json_file = open("mnist_model.json", "w")
#json_file.write(model_json)
#json_file.close()


#model.save_weights('my_model_weights.h5')




