import Classificator.Learn_neiro.Module_MySQL as SQL
import re
import string
from pymorphy2.tokenizers import simple_word_tokenize
import os
import shutil

class state_machine: #МП для реализации логии
    __state=''
    tem=''

    def __init__(self,new_state):
        self.__state=new_state

    def new_state(self,new_state):
        self.__state=new_state

    def show_state(self):
        return self.__state

    def next_state(self,action,string):
            spisk = ['A', 'E', 'F']
            if (self.__state == 'B' and action == 'A_N_A'):
                self.__state = 'F'
                return
            if (self.__state == 'B' and action == 'A_C'):
                self.__state = 'C'
                return
            if (self.__state == 'B' and action == 'A_A'):
                self.__state = 'D'
                return
            if (self.__state == 'B' and action == 'A_N_C'):
                self.__state = 'E'
                return
            if (self.__state == 'C' and action == 'A_N_T'):
                self.__state = 'B'
                return
            if (self.__state == 'D' and action == 'A_N_T'):
                self.__state = 'B'
                return
            if (self.__state in spisk and action == 'A_N_T'):
                self.__state = 'B'
                return
            if (self.__state in spisk and action == 'A_C'):
                self.__state = 'C'
                return
            if (self.__state in spisk and action == 'A_A'):
                self.__state =  'D'
                return
            if (self.__state == 'E' and action == 'A_N_A'):
                self.__state = 'F'
                return
            if (self.__state == 'F' and action == 'A_N_C'):
                self.__state = 'E'
                return
            if (self.__state == 'C' and action == 'A_A'):
                self.__state = 'D'
                return
            if (self.__state == 'D' and action == 'A_C'):
                self.__state = 'C'
                return
            if (self.__state == 'D' and action == 'A_A'):
                self.__state = 'D'
                return
            if (self.__state == 'C' and action == 'A_C'):
                self.__state = 'C'
                return

            print('Конструкция <',string,'> недопустима')
            print('Добавление невозможно')
            exit()




conn=SQL.connect()
cursor = conn.cursor()

#directory='C:\Учеба/3_курс\Интелектуальный_интернет\Программы\python\MyProject\For_append/'
Path_to_dir = os.getcwd()
Path_to_prog = Path_to_dir.replace("\Classificator", '')
directory = Path_to_prog + "\DATA\For_append/"

#files=os.listdir(directory)
files=[f for f in os.listdir(directory) if f.endswith('.txt')]
#print(files)
#file="C:\Учеба/3_курс\Интелектуальный_интернет\Программы\python\MyProject\For_append\Append.txt" #файлы с добавлением
sent_tokenize = re.compile("\n").split #для разделения по строкам

for file in files:
    with open(directory+file, 'rt', encoding='cp1251') as f: #открываем файл
         text = f.read()  #присваеваем строке прочитанный файл
    #print(text)
    #state='A'#состояние
    automat=state_machine('A')
    #print(automat.show_state())

    #print(simple_word_tokenize(text.strip()))
    #for string in simple_word_tokenize(text.strip()):

    COMMANDS_APPEND=[ #возможные команды добавления в БД
        "_APPEND_NEW_TEM_","_APPEND_CONST","_APPEND_ANSWER"
    ]

    def check_command(count_string):
        count = 0
        while count < 3:  # проходим по всевозможным командам
            if (COMMANDS_APPEND[count] in strings[count_string]):  # если команда входит в строку,то;
                if (count == 0):  # если это _APPEND_NEW_TEM_ (добавление новой темы)
                    # print(strings[count_string+1])
                    #automat.new_state('B')
                    automat.next_state('A_N_T',strings[count_string])
                    return True
                if (count == 1):  # если это _APPEND_CONST (добавление языковой конструкции)
                    new_string = simple_word_tokenize(strings[count_string])
                    #print(len(new_string))
                    #automat.new_state('C')
                    if(len(new_string)==2):
                        automat.next_state('A_C',strings[count_string])
                        automat.tem = new_string[1]
                    elif (len(new_string)==1):
                        automat.next_state('A_N_C',strings[count_string])
                    else:
                        print('Конструкция <',new_string,'> недопустима')
                        print('Добавление невозможно.')
                        exit()
                    return True
                if (count == 2):  # если это _APPEND_ANSWER (добавление ответа на конструкцию)
                    new_string = simple_word_tokenize(strings[count_string])
                    #print(len(new_string))
                    #automat.new_state('D')
                    if(len(new_string)==2):
                        automat.next_state('A_A',strings[count_string])
                        automat.tem=new_string[1]
                    elif (len(new_string)==1):
                        automat.next_state('A_N_A',strings[count_string])
                    else:
                        print('Конструкция <',new_string,'> недопустима')
                        print('Добавление невозможно.')
                        exit()
                    return True
            count = count + 1






    strings=sent_tokenize(text) #разбиваем строку на подстроки(будет список)
    count_string=0
    len_strings=len(strings)#узнаем длину списка
    #print(strings)
    #print(len_strings)
    command_for_BD=[]
    count_command=0
    count_new_tem=0
    while count_string<len_strings: #проходим по всем строкам файла
        #Проверка на команды
        if(check_command(count_string)==True):
            #print(strings[count_string], ' ', automat.show_state())
            count_string = count_string + 1
            count_command=0
            continue
        #print(strings[count_string], ' ', automat.show_state())
        if(not strings[count_string]==''):
            if(automat.show_state()=='B'): #добавление новой темы
                #print(strings[count_string])
                if(count_new_tem>0):
                    print("В _APPEND_NEW_TEM_ допустима только одна тема")
                    print("Добавление невозможно")
                    exit()
                command=['Append_tem',strings[count_string].strip()]
                command_for_BD.append(command)
                count_new_tem=count_new_tem+1
            else:
                count_new_tem=0

            if (automat.show_state() == 'E'): #добавление конструкций к существующим темам
                command = ['Append_new_const',strings[count_string].strip()]
                command_for_BD.append(command)
            if (automat.show_state() == 'F'): #добавление конструкций к существующим темам
                command = ['Append_new_answ',strings[count_string].strip()]
                command_for_BD.append(command)
            if (automat.show_state() == 'C'): #добавление конструкций к существующим темам
                command = ['Append_const',strings[count_string].strip(), automat.tem]
                command_for_BD.append(command)
            if (automat.show_state() == 'D'): #добавление ответов к существующим темам
                command = ['Append_answ',strings[count_string].strip(), automat.tem]
                command_for_BD.append(command)
            count_command=count_command+1
        else:
            if(count_command==0):
                print('Строка',count_string+1,'является пустой.')
                print('Добавление невозможно.')
                exit()
        count_string=count_string+1

    #print(command_for_BD)
    #while True:
    #    pass
    cursor.execute("START TRANSACTION;") #для отката

    for command in command_for_BD:
        if(command[0]=='Append_const'):
            cursor.execute("""
                    SELECT EXISTS(
                    SELECT Id_const FROM waifu.lang_const
                    WHERE Id_const=%s
                     )"""
                           , (command[2],))
            for curs in cursor:
                if(curs[0]==0):
                    print('Невозможно добавить конструкцию <',command[1],'> т.к. темы №',command[2],'не существует.')
                    print('Внесите изменение и перезапустите скрипт')
                    cursor.execute('ROLLBACK;')
                    exit()
                else:
                    cursor.execute("""
                            INSERT waifu.text_const(Text_const,Id_const)
                                    Values (%s,%s)
                    """,(command[1],command[2],)
                    )

        if(command[0]=='Append_answ'):
            cursor.execute("""
                            SELECT EXISTS(
                            SELECT Id_const FROM waifu.lang_const
                            WHERE Id_const=%s
                             )"""
                           , (command[2],))
            for curs in cursor:
                if (curs[0] == 0):
                    print('Невозможно добавить ответ <', command[1], '> т.к. темы №', command[2], 'не существует.')
                    print('Внесите изменение и перезапустите скрипт')
                    cursor.execute('ROLLBACK;')
                    exit()
                else:
                    cursor.execute("""
                                    INSERT waifu.answer_const(Text_answer,Id_const)
                                            Values (%s,%s)
                            """, (command[1], command[2],)
                                   )
        if(command[0]=='Append_tem'):
            cursor.execute("""
                        INSERT waifu.lang_const(Name_const)
                                Values (%s)
            """,(command[1],))
            #new_tem=command[1]
            #id_new_tem=
            cursor.execute("""
                                SELECT Id_const FROM waifu.lang_const
                                        WHERE Name_const=%s
                    """, (command[1],))
            for curs in cursor:
                id_new_tem_const=curs[0]

        if(command[0]=='Append_new_const'):
            cursor.execute("""
                    INSERT waifu.text_const(Text_const,Id_const)
                            Values (%s,%s)
            """, (command[1], id_new_tem_const,)
                           )

        if (command[0] == 'Append_new_answ'):
            cursor.execute("""
                                            INSERT waifu.answer_const(Text_answer,Id_const)
                                                    Values (%s,%s)
                                    """, (command[1], id_new_tem_const,)
                           )

    cursor.execute("COMMIT;")
    shutil.move(directory+file,directory+'Appended')
    print('Файл ',file,'добавлен.')

conn.close()






