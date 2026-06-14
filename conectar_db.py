import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

BANCO = "mercado.db"
DIR = os.path.dirname(os.path.abspath(__file__))
BANCO = os.path.join(DIR, "Dados", BANCO)
BANCO_URL = f"sqlite:///{BANCO}"

def verificar_db():
    if not os.path.exists(BANCO):
        print("Erro: banco não existe")
        exit()

engine = create_engine(BANCO_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

#verificar_db()