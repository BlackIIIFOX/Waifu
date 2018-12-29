import Classificator.Learn_neiro.lemmatization as lemmatization
from gensim.models import Word2Vec, Phrases
import gensim.models
import os
import Cython
import Classificator.Learn_neiro.Module_MySQL as SQL



def create(conn,Path_to_prog):
        cursor = conn.cursor()
        cursor.execute("SELECT Text_const FROM  Waifu.text_const;")
        try:
           #sents = lemmatization.get_sents(text_const) #разбивает строку и приводит каждое слово строки к нормальной форме
           sents = lemmatization.get_sents_for_create(cursor)
        except:
            print('Лемантизация невозможная')
            exit()

        print('Этап лемантизации пройден')

        try:
           bigram_transformed = Phrases(sents)
           w2v= Word2Vec(bigram_transformed[sents],window=5,min_count=1,size=40,workers=4)  #cbow_mean=2
           w2v.init_sims(replace=True)
           w2v.save(Path_to_prog+'\DATA\\Neiro\w2v_vectors.model')
        except:
            print('Создание модели невозможно')
            exit()


        print('Создание модели w2v проведено')
        return w2v

        #show_model.plot()







