from gensim.models import Word2Vec
import Classificator.Learn_neiro.lemmatization as lemmatization
import os
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
import Classificator.Learn_neiro.text_in_vec as text_in_vec




def neiro(conn,w2v_model,Path_to_prog):
        #грузим векторное пространство
        #w2v_model = Word2Vec.load('all_vectors.model')
        #w2v_model.init_sims(replace=True)

        input_output=text_in_vec.for_train(w2v_model,conn)
        #print(len(input_output[1]))

        print('Выборка переведена в допустимый формат')

        neiro_model = Sequential()
        neiro_model.add(Dense(70, input_dim=40, activation='relu'))
        neiro_model.add(Dense(35, activation='relu'))
        neiro_model.add(Dense(15, activation='relu'))
        neiro_model.add(Dense(input_output[2], activation='sigmoid'))

        neiro_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        neiro_model.fit(input_output[0], input_output[1], epochs=600, batch_size=2,verbose=2)


        # Генерируем описание модели в формате json
        model_json = neiro_model.to_json()
        # Записываем модель в файл
        json_file = open(Path_to_prog+"\DATA\\Neiro\mnist_model.json", "w")
        json_file.write(model_json)
        json_file.close()

        neiro_model.save_weights(Path_to_prog+"\DATA\\Neiro\my_model_weights.h5")
        print('Нейро обучена')


