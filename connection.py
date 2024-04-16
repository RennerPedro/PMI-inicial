from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker

# Configuracao
engine = create_engine("mysql://root:12345@localhost:3306/pmi")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entindades 
class Usuario():
    __tablename__ = "Usuario"

    idusuario = Column(String, primary_key=False)
    nome = Column(String, nullable=False)
    cpf = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(Integer, nullable=False)
    data_de_nascimento = Column(Date, nullable=False)
    senha = Column(String, nullable=False)

    def __repr__(self): #estetica
        return f"Usuario dados (Nome={self.nome}, cpf={self.cpf}, email={self.email}, telefone={self.telefone}, nacimento={self.data_de_nascimento}, senha={self.senha})"

# SQL

#select
data =session.query(Usuario).all()
print(data)  

#delet
session.query(Usuario).filter(Usuario.nome=="lucas").delete()
session.commit()

#update
session.query(Usuario).filter(Usuario.cpf=="12795049945").update({"email":"oi"})
session.commit()

#insert
data_isert = Usuario(nome="lucas", cpf="12795049945")
session.add(data_isert)


session.commit()
session.close







