import Classificator.Learn_neiro.create_model as create_model
import Classificator.Learn_neiro.model as model
import Classificator.Learn_neiro.Module_MySQL as SQL
import os

#try:
def learn_neiro(conn,Path_to_prog):
    print("Создание векторного пространства")
    w2v_model = create_model.create(conn,Path_to_prog)
    print("Обучение нейросети")
    model.neiro(conn,w2v_model,Path_to_prog)
    print("\nОбучение завершено")


if __name__ == '__main__':
    Path_to_dir = os.getcwd()
    Path_to_prog = Path_to_dir.replace("\Classificator\Learn_neiro", '')
    conn = SQL.connect()
    learn_neiro(conn,Path_to_prog)
    conn.close()
