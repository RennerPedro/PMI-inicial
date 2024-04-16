from infra.configs.conection import DBConnectionHandler
from infra.entities.usuario import Usuario

class UsuarioRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Usuario).all()
            return data 