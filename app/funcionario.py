class Funcionario:
    def __init__(self, dict):

        self.nome = dict["nome"]
        self.registro = dict["registro"]
        self.senha = dict["senha"]
        self.email = dict["email"]
        self.telefone = dict["telefone"]
        self.status = dict["status"]
        self.data_nascimento = dict["nascimento"]