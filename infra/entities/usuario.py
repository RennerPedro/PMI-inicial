from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Date

class Usuario(Base):
    __tablename__ = "Usuario"

    idusuario = Column(String, primary_key=True)  
    nome = Column(String, nullable=False)
    cpf = Column(Integer, nullable=False, unique=True)  
    email = Column(String, nullable=False)
    telefone = Column(Integer, nullable=False)
    data_de_nascimento = Column(Date, nullable=False)
    senha = Column(String, nullable=False)

    def __repr__(self):
        return f"Usuario dados (Nome={self.nome}, cpf={self.cpf}, email={self.email}, telefone={self.telefone}, nacimento={self.data_de_nascimento}, senha={self.senha})"
