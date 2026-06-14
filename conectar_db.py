import os.path
import sqlite3

BANCO = "mercado.db"
DIR = os.path.dirname(os.path.abspath(__file__))
BANCO = os.path.join(DIR, "Dados", BANCO)


def verificar_db():
    if not os.path.exists(BANCO):
        print("Erro: banco não existe")
        exit()

def connect():
    try:
        return sqlite3.connect(BANCO)
    except Exception as ex:
        raise Exception(f"Erro: {ex}")

def disconnect(conn):
    if conn:
        conn.close()


#print(verificar_db())
