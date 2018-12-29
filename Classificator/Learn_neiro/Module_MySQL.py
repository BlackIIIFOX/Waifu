import mysql.connector as MySQLdb
from mysql.connector import Error

def connect(): #соединеие с БД
    try:
        print('Connecting to MySQL database...')
        conn = MySQLdb.connect(host='localhost', database='waifu', user='root', password='h8970102742', use_unicode=True, charset ='utf8')
        print("Connection established")
        return conn
    except Error as e:
        print(e)
        exit()

def not_connect(conn):
    conn.close()
    exit()

if __name__ == '__main__':
    conn = connect()
    conn.close(conn)


