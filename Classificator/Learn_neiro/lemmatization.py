import re
import string
from pymorphy2.tokenizers import simple_word_tokenize
from pymorphy2 import MorphAnalyzer


stopwoards = set(string.punctuation) | {'_','—','–','−','_tem'}
morph= MorphAnalyzer()
sent_tokenize = re.compile("[.,?!'\'\n]").split

def best_parser(token,parses):
    for p in parses:
        if token.istitle() and {'Geox', 'Name', 'Surn', 'Patr'} & p.tag.grammemes:#если с большой буквы и входит в теги одушевл.:                                                        #Geox-георгрифия,Name-имя,Surn-фамилия
            return p#оставляем в той же форме                                     #Patr-отчество
        if p.tag.POS == 'NPRO': #если местоимение(NPRO-местоимение)
            return p
        return parses[0]


#приведение в нормальную форму
def normal_form(p):
    if {'Patr', 'Surn'} & p.tag.grammemes:#если это Фамилия или отчество
        #print(p.word)
        #print(p.inflect({'sing', 'nomn'}).word)
        return p.inflect({'sing', 'nomn'}).word #склоняет в sign-единственное число,nomn-именительный падеж и возвращает
    return p.normal_form #слово приводит в нормальную

#ф-ия нормализации слова:
def normalized(tokens):
    #нормализуем каждый токен в зависимости от надобности
    parser = [
        #print(morph.parse(w))
        best_parser(w, morph.parse(w))
        for w in tokens
        if w.lower() not in stopwoards
    ]

    #убирает токены,которые не соответсвуют частям речи
    parser = [
        p for p in parser
        #if p.tag.POS not in {'PNCT', 'LATN', 'CONJ', 'NUMB', 'PREP'}#CONJ-союз,#PNCT-пунктуация,NUMB-число,LATN-токен состоит из лат.букв
        if not {'PNCT', 'CONJ', 'NUMB,real', 'NUMB', 'NUMB,intg', 'PREP', 'UNKN'} & p.tag.grammemes
    ]
    #возвращает нормальную форму слова,приведенного в нижний регистр
    #print(normal_form(p).lower() for p in parser)
    return [normal_form(p).lower() for p in parser]


#Ф-ИЯ ДЛЯ РАЗБИЕНИЯ СТРОКИ НА ТОКЕНЫ И ПЕРЕДАЧА В Ф-ИЮ НОРМАЛИЗАЦИИ
#делит единую строку на отдельные строки,а так же
#убирает из строки разделители,которые заданы регулярным выражением sent_tokenize с помощью библиотеки re.
#После чего убирает из начала и конца строки пробелы(sent.strip()) с пом. библиотеки string и ее метода strip
#и передает в ф-ию нормализации список из токенов с пом. библиотеки pymorphy2 и метода simple_word_tokenize
#                              пример:
#вход(book)-" Я ничего не понимаю,  может  быть"
#параметр передаваем в ф-ию normalized: ['Я', 'ничего', 'не', 'понимаю'],['может', 'быть']
def get_sents(book):
    return [
        normalized(simple_word_tokenize(sent.strip()))
        for sent in sent_tokenize(book) if sent.strip()
        #normalized(simple_word_tokenize(book))
    ]

def get_sents_for_create(cursor):
    return [
        #normalized(simple_word_tokenize(sent))
        normalized((simple_word_tokenize(sent[0])))
        for sent in cursor
    ]